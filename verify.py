"""Vérificateur de référence PUCIA-0001, version 0.1.0.

Vérifie un paquet de configuration PUCIA décompressé dans un répertoire,
selon les contrôles V1 à V9 de la norme PUCIA-0001.

Usage :
    python verify.py <répertoire_du_paquet> <schéma_json>

Code de sortie : 0 si le paquet est conforme, 1 sinon.

Le résultat atteste la structure, l'intégrité (V8) et la présence des preuves
d'horodatage (V9). La validité des preuves relève de PUCIA-0002 et l'identité
du publieur de PUCIA-0003.
"""

import base64
import hashlib
import json
import sys
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from jsonschema import Draft202012Validator


def canonical(obj) -> bytes:
    """Sérialisation canonique JSON (RFC 8785) pour les types utilisés par PUCIA-0001."""
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(package_dir: Path, schema_path: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = package_dir / "manifest.json"

    # V1 — présence et lecture du manifeste
    if not manifest_path.is_file():
        return ["V1 : manifest.json absent"]
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"V1 : manifeste illisible ({exc})"]

    # V2 — conformité au schéma
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        schema, format_checker=Draft202012Validator.FORMAT_CHECKER
    )
    for err in sorted(validator.iter_errors(manifest), key=lambda e: list(e.path)):
        location = "/".join(str(p) for p in err.path) or "(racine)"
        errors.append(f"V2 : {location} : {err.message}")
    if errors:
        return errors

    # V3 — aucun fichier hors de la structure autorisée, aucun lien symbolique
    allowed_roots = {"manifest.json", "artifacts", "signatures", "timestamps"}
    for item in package_dir.rglob("*"):
        rel = item.relative_to(package_dir)
        if item.is_symlink():
            errors.append(f"V3 : lien symbolique interdit : {rel}")
        if rel.parts[0] not in allowed_roots:
            errors.append(f"V3 : élément non autorisé : {rel}")

    # V4 — artefacts déclarés : présence, taille, empreinte
    declared = set()
    for art in manifest["artifacts"]:
        path = package_dir / art["path"]
        declared.add(Path(art["path"]))
        if not path.is_file():
            errors.append(f"V4 : artefact absent : {art['path']}")
            continue
        data = path.read_bytes()
        if len(data) != art["size_bytes"]:
            errors.append(f"V4 : taille incorrecte : {art['path']}")
        if sha256_hex(data) != art["sha256"]:
            errors.append(f"V4 : empreinte incorrecte : {art['path']}")

    # V5 — aucun artefact non déclaré
    art_dir = package_dir / "artifacts"
    if art_dir.is_dir():
        for item in art_dir.rglob("*"):
            if item.is_file() and item.relative_to(package_dir) not in declared:
                errors.append(f"V5 : artefact non déclaré : {item.relative_to(package_dir)}")

    # V6 — empreinte agrégée des artefacts
    if sha256_hex(canonical(manifest["artifacts"])) != manifest["artifact_hash"]:
        errors.append("V6 : artifact_hash ne correspond pas aux artefacts déclarés")

    # V7 — cohérence du budget de paramètres
    budget = manifest["parameter_budget"]
    if budget["base_total"] != manifest["base_model_parameters"]:
        errors.append("V7 : parameter_budget.base_total diffère de base_model_parameters")
    if budget["active"] > budget["base_total"] + budget["added_total"]:
        errors.append("V7 : paramètres actifs supérieurs au total déclaré")
    if manifest["config_type"] == "mask" and budget["added_total"] != 0:
        errors.append("V7 : une configuration de type mask ne doit ajouter aucun paramètre")

    # V8 — signature Ed25519 sur le manifeste canonique (intégrité, non identité)
    sig_path = package_dir / manifest["signature"]["file"]
    if not sig_path.is_file():
        errors.append("V8 : fichier de signature absent")
    else:
        try:
            public_key = Ed25519PublicKey.from_public_bytes(
                base64.b64decode(manifest["signature"]["public_key"], validate=True)
            )
            signature = base64.b64decode(sig_path.read_text(encoding="ascii").strip(), validate=True)
            public_key.verify(signature, canonical(manifest))
        except (InvalidSignature, ValueError):
            errors.append("V8 : signature invalide")

    # V9 — présence des preuves d'horodatage déclarées (validité : PUCIA-0002)
    for proof in manifest["timestamp_proof"]:
        if not (package_dir / proof["file"]).is_file():
            errors.append(f"V9 : preuve d'horodatage absente : {proof['file']}")

    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    errors = verify(Path(sys.argv[1]), Path(sys.argv[2]))
    if errors:
        print("NON CONFORME")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("CONFORME PUCIA-0001 (contrôles V1 à V9)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
