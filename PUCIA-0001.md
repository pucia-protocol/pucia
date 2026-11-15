# PUCIA-0001 — Format du paquet de configuration et du manifeste

| | |
|---|---|
| **Norme** | PUCIA-0001 |
| **Version** | 0.1.0 |
| **Statut** | Projet de norme |
| **Date** | 15 novembre 2026 |
| **Auteur et mainteneur** | Honoré DEMBELE |
| **Licence** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Remplace** | Néant |
| **Fichiers normatifs associés** | `pucia-0001-manifest.schema.json` (schéma du manifeste) |
| **Implémentation de référence** | `verify.py` (vérificateur de conformité) |

## Résumé

La présente norme définit le format d'un **paquet de configuration PUCIA** : la structure de l'archive, le contenu obligatoire du manifeste, le calcul des empreintes, la signature et la déclaration des preuves d'horodatage. Elle définit également les neuf contrôles qu'un vérificateur DOIT exécuter pour déclarer un paquet conforme. Un paquet conforme peut être publié, échangé, vérifié et activé par toute IA ou tout logiciel compatible avec PUCIA.

## 1. Objet et domaine d'application

1.1. La présente norme s'applique à tout paquet destiné à être publié dans un registre PUCIA ou échangé entre systèmes se déclarant compatibles avec PUCIA.

1.2. Elle ne définit pas l'attribution des identifiants OID ni la validation des preuves d'horodatage, qui relèvent de PUCIA-0002. Elle ne définit pas la procédure de certification, qui relève de PUCIA-0003, ni les interfaces du registre, qui relèvent de PUCIA-0004.

## 2. Conventions

2.1. Les mots **DOIT**, **NE DOIT PAS**, **DEVRAIT**, **NE DEVRAIT PAS** et **PEUT**, écrits en majuscules, ont dans la présente norme le sens respectif des mots MUST, MUST NOT, SHOULD, SHOULD NOT et MAY définis par les RFC 2119 et RFC 8174.

2.2. Une exigence exprimée par DOIT ou NE DOIT PAS est vérifiable par un contrôle de la section 9. Un paquet qui en méconnaît une seule est non conforme.

## 3. Définitions

- **Paquet** : archive contenant une configuration et l'ensemble des éléments nécessaires à sa vérification.
- **Manifeste** : fichier `manifest.json` décrivant le paquet.
- **Artefact** : fichier contenant la configuration proprement dite : masque, table de routage, adaptateur, vecteur de tâche, politique ou prédicteur.
- **Modèle de base** : modèle dont les poids exacts sont identifiés par leur empreinte et auquel la configuration s'applique.
- **Publieur** : personne physique ou morale, ou agent agissant pour son compte, qui signe le paquet.
- **Forme canonique** : sérialisation d'un objet JSON selon la RFC 8785 (JSON Canonicalization Scheme).
- **Empreinte** : condensat SHA-256 (FIPS 180-4) exprimé en 64 caractères hexadécimaux minuscules.

## 4. Structure du paquet

4.1. Un paquet DOIT être une archive au format POSIX.1-2001 (pax), non compressée, portant l'extension `.pucia`.

4.2. L'archive DOIT contenir, à sa racine, exactement les éléments suivants :

```text
manifest.json             manifeste du paquet
artifacts/                artefacts de la configuration
signatures/manifest.sig   signature du manifeste
timestamps/               preuves d'horodatage
```

4.3. L'archive NE DOIT contenir aucun autre élément à sa racine, aucun lien symbolique ou physique, et aucun chemin comportant le segment `..`.

4.4. Chaque fichier présent dans `artifacts/` DOIT être déclaré dans le manifeste, et chaque artefact déclaré DOIT être présent.

4.5. Un vérificateur PEUT refuser un paquet dont la taille totale dépasse la limite qu'il publie ; il DOIT alors indiquer cette limite dans son message de refus.

## 5. Manifeste

5.1. Le manifeste DOIT être un document JSON (RFC 8259) encodé en UTF-8, sans marque d'ordre des octets.

5.2. Le manifeste DOIT être valide au regard du schéma `pucia-0001-manifest.schema.json`, qui fait partie intégrante de la présente norme. Il NE DOIT contenir aucun champ non défini par ce schéma, à l'exception du contenu de l'objet `extensions` (section 5.5).

5.3. Les nombres décimaux NE DOIVENT figurer que dans les champs `score`, `baseline_score` et `amount`. Tous les autres nombres DOIVENT être des entiers.

5.4. Le tableau suivant récapitule les champs. En cas de divergence, le schéma prévaut.

| Champ | Type | Exigence |
|---|---|---|
| `pucia_spec` | chaîne | DOIT valoir `PUCIA-0001`. |
| `protocol_version` | chaîne | DOIT valoir `0.1.0` pour la présente version. |
| `pucia_oid` | chaîne | Identifiant OID de la configuration, sous l'arc `1.3.6.1.4.1`, attribué selon PUCIA-0002. |
| `name` | chaîne | Nom lisible de la configuration, 128 caractères au plus. |
| `version` | chaîne | Version de la configuration au format `majeur.mineur.correctif`. |
| `created` | chaîne | Date et heure de création au format RFC 3339, en temps universel (suffixe `Z`). |
| `publisher` | objet | `name` et `contact` (adresse électronique) du publieur. |
| `config_type` | énumération | `mask`, `routing`, `adapter`, `task_vector`, `policy` ou `predictor`. |
| `base_model_id` | chaîne | Identifiant du modèle de base. |
| `base_hash` | empreinte | Empreinte des poids exacts du modèle de base. |
| `tokenizer_hash` | empreinte | Facultatif. Empreinte du tokeniseur. |
| `base_model_license` | chaîne | Identifiant SPDX de la licence du modèle de base. |
| `base_model_parameters` | entier | Nombre total de paramètres du modèle de base. |
| `artifacts` | tableau | Un objet par artefact : `path`, `sha256`, `size_bytes`, `media_type`. |
| `artifact_hash` | empreinte | Empreinte de la forme canonique du tableau `artifacts` (section 6.2). |
| `parameter_budget` | objet | `base_total`, `added_total`, `active`, `storage_bytes` et, facultativement, `external_bytes` (section 7). |
| `signature` | objet | `algorithm` (`Ed25519`), `public_key` (clé publique en base64), `file` (`signatures/manifest.sig`). |
| `timestamp_proof` | tableau | Au moins une preuve : `format` (`RFC3161` ou `OpenTimestamps`) et `file`. |
| `task_spec` | objet | `task_id`, `description`, `languages` (étiquettes BCP 47) et, facultativement, `restrictions`. |
| `benchmark_manifest` | tableau | Au moins un banc : `name`, `version`, `dataset_hash`, `metric`, `score` et, facultativement, `baseline_score`. |
| `license` | chaîne | Identifiant SPDX ou `LicenseRef-` de la licence de la configuration. |
| `pricing` | objet | `model` (`free` ou `paid`) ; si `paid`, `currency` (code ISO 4217) et `amount` sont obligatoires. |
| `provenance` | objet | `method`, `training_data`, `data_rights` et, facultativement, `dependencies` (OID des configurations utilisées). |
| `lifecycle` | énumération | `active`, `deprecated`, `migrated` ou `revoked`. |
| `migration` | objet | `commitment` ; si vrai, `delay_days` est obligatoire ; si `lifecycle` vaut `migrated`, `successor_oid` est obligatoire. |
| `safety` | objet | `risks` (risques identifiés) et `tests` (au moins un test de sécurité ou de régression effectué). |
| `rollback` | objet | `procedure` de retour à l'état antérieur. |
| `extensions` | objet | Facultatif. Champs propres à un publieur ou à une expérimentation (section 5.5). |

5.5. L'objet facultatif `extensions` PEUT contenir des champs non définis par la présente norme. Le nom de chacun de ces champs DOIT commencer par un nom de domaine inversé ou un OID contrôlé par le publieur, suivi d'un point (par exemple `org.example.qualite`). Un vérificateur DOIT ignorer le contenu de `extensions` pour la décision de conformité, à l'exception de son inclusion dans la forme canonique signée.

## 6. Empreintes

6.1. Toutes les empreintes DOIVENT être calculées par SHA-256 et exprimées en hexadécimal minuscule.

6.2. Le champ `artifact_hash` DOIT être l'empreinte de la forme canonique (RFC 8785) du tableau `artifacts`, tel qu'il figure dans le manifeste.

6.3. L'empreinte d'un artefact DOIT porter sur le contenu exact du fichier, octet par octet.

## 7. Budget de paramètres

7.1. `parameter_budget.base_total` DOIT être égal à `base_model_parameters`.

7.2. `parameter_budget.added_total` DOIT déclarer le nombre de paramètres que la configuration ajoute au modèle de base. Pour une configuration de type `mask`, il DOIT être égal à zéro.

7.3. `parameter_budget.active` DOIT déclarer le nombre de paramètres effectivement utilisés une fois la configuration activée. Il NE DOIT PAS dépasser la somme de `base_total` et de `added_total`.

7.4. `parameter_budget.storage_bytes` DOIT déclarer l'espace de stockage propre à la configuration. Il DEVRAIT être égal à la somme des tailles des artefacts.

7.5. Si la configuration recourt à une mémoire ou une base externe, `parameter_budget.external_bytes` DOIT en déclarer le volume.

## 8. Signature et horodatage

8.1. Le manifeste DOIT être signé par l'algorithme Ed25519 (RFC 8032).

8.2. La signature DOIT porter sur la forme canonique (RFC 8785) du manifeste complet, tel qu'il figure dans `manifest.json`. Le manifeste ne contenant pas la valeur de la signature, aucune circularité n'est possible.

8.3. Le fichier `signatures/manifest.sig` DOIT contenir la signature de 64 octets encodée en base64 (RFC 4648), suivie facultativement d'un saut de ligne.

8.4. Le paquet DOIT contenir au moins une preuve d'horodatage de l'empreinte de la forme canonique du manifeste, au format RFC 3161 (fichier `.tsr`) ou OpenTimestamps (fichier `.ots`), placée dans `timestamps/` et déclarée dans `timestamp_proof`.

8.5. La validation cryptographique des preuves d'horodatage est définie par PUCIA-0002.

8.6. La signature prouve l'intégrité du manifeste et sa production par le détenteur de la clé privée correspondant à `signature.public_key`. Elle ne prouve pas l'identité du publieur : toute personne peut engendrer une paire de clés et signer un paquet. L'identité du publieur est attestée par le registre PUCIA, qui associe la clé publique à une personne identifiée, selon PUCIA-0003.

## 9. Contrôles de conformité

Un vérificateur DOIT exécuter les contrôles suivants. Le paquet est conforme si et seulement si aucun contrôle n'échoue.

| Contrôle | Objet |
|---|---|
| **V1** | `manifest.json` est présent et constitue un document JSON valide encodé en UTF-8. |
| **V2** | Le manifeste est valide au regard du schéma normatif. |
| **V3** | Le paquet ne contient aucun élément hors de la structure de la section 4.2 et aucun lien. |
| **V4** | Chaque artefact déclaré est présent, et sa taille et son empreinte correspondent au manifeste. |
| **V5** | Aucun fichier de `artifacts/` n'est absent du manifeste. |
| **V6** | `artifact_hash` correspond à la forme canonique du tableau `artifacts`. |
| **V7** | Le budget de paramètres respecte les règles de la section 7. |
| **V8** | La signature Ed25519 du manifeste canonique est valide pour la clé publique déclarée (intégrité). |
| **V9** | Chaque preuve d'horodatage déclarée est présente dans le paquet (présence). |

Le résultat « CONFORME PUCIA-0001 » atteste la structure du paquet, l'intégrité de son contenu et la présence des preuves d'horodatage. Il n'atteste ni la validité cryptographique de ces preuves, établie selon PUCIA-0002, ni l'identité du publieur, attestée selon PUCIA-0003, ni la qualité de la configuration, établie par la certification.

## 10. Activation et compatibilité

10.1. Un système NE DOIT PAS activer une configuration sur un modèle dont l'empreinte des poids diffère de `base_hash`.

10.2. Si `tokenizer_hash` est présent, un système NE DOIT PAS activer la configuration avec un tokeniseur dont l'empreinte diffère.

10.3. Un système NE DOIT PAS activer une configuration dont `lifecycle` vaut `revoked`. Il DEVRAIT avertir son utilisateur avant d'activer une configuration dont `lifecycle` vaut `deprecated`.

10.4. Un système NE DOIT PAS activer une configuration dont le paquet échoue à l'un des contrôles de la section 9.

## 11. Sécurité

11.1. Un vérificateur DOIT extraire l'archive dans un répertoire isolé et refuser tout chemin absolu, tout segment `..` et tout lien avant extraction.

11.2. Un artefact NE DOIT PAS contenir de code exécutable destiné à être chargé par désérialisation arbitraire. Les artefacts DEVRAIENT utiliser un format de tenseurs sans exécution de code. Cette exigence relève de l'audit de certification et n'est pas vérifiée par les contrôles V1 à V9.

11.3. La clé privée du publieur NE DOIT PAS figurer dans le paquet.

## 12. Versionnement de la norme

12.1. Toute modification incompatible du schéma entraîne l'incrémentation du numéro majeur de `protocol_version`. L'ajout d'un champ facultatif au schéma entraîne l'incrémentation du numéro mineur. Les champs placés dans `extensions` n'entraînent aucun changement de version.

12.2. Un vérificateur DOIT refuser un paquet dont la `protocol_version` ne correspond à aucune version qu'il implémente.

## Annexe A — Exemple de paquet conforme

Le sous-répertoire `exemple-masque-extraction/`, livré avec la présente norme, contient un paquet complet, signé, déclaré conforme par le vérificateur de référence. Il utilise le numéro d'entreprise privée 32473, réservé par l'IANA à la documentation (RFC 5612), et le domaine `example.org`, réservé à la documentation (RFC 2606). Sa preuve d'horodatage est un fichier d'illustration : il satisfait le contrôle de présence V9 et ne constitue pas une preuve valide au sens de PUCIA-0002, ce qui illustre la portée exacte du résultat de conformité (section 9).

Le paquet décrit un masque binaire de 4 096 octets, soit 32 768 bits, appliqué à la couche 12 d'un modèle de base de 1,5 milliard de paramètres, pour une tâche d'extraction de données de factures. Conformément à la section 7.2, il n'ajoute aucun paramètre.

```json
{
  "pucia_spec": "PUCIA-0001",
  "protocol_version": "0.1.0",
  "pucia_oid": "1.3.6.1.4.1.32473.1.1",
  "name": "Extraction de données de factures",
  "version": "1.0.0",
  "created": "2026-11-14T22:00:00Z",
  "publisher": {
    "name": "Exemple Labs",
    "contact": "contact@example.org"
  },
  "config_type": "mask",
  "base_model_id": "exemple/modele-base-1.5b",
  "base_hash": "7e1d1270e83fec3b46e495f2c85de5dc505c25efa5a6e4c184fe4d25ab6f5832",
  "tokenizer_hash": "d1dbfd21894c27cd81f88950cb4cfe354f6269d0c39311a8b7c8c834949021f2",
  "base_model_license": "Apache-2.0",
  "base_model_parameters": 1500000000,
  "artifacts": [
    {
      "path": "artifacts/masque-couche-12.bin",
      "sha256": "571747de0defe8e9facd3246ad09d3897cd619d1e31c8815c3248c0f3c293f9b",
      "size_bytes": 4096,
      "media_type": "application/octet-stream"
    }
  ],
  "artifact_hash": "28940b651f75a8a365fe317e9028012efa7ed12aa505fb0d44a0bd62a055f656",
  "parameter_budget": {
    "base_total": 1500000000,
    "added_total": 0,
    "active": 1499983616,
    "storage_bytes": 4096
  },
  "signature": {
    "algorithm": "Ed25519",
    "public_key": "p4sLKjKLEHStLQoAy7ooxNxvjlrh2nAs4kHE7KzEGh0=",
    "file": "signatures/manifest.sig"
  },
  "timestamp_proof": [
    {
      "format": "OpenTimestamps",
      "file": "timestamps/manifest.ots"
    }
  ],
  "task_spec": {
    "task_id": "extraction-factures",
    "description": "Extraire d'une facture le fournisseur, la date, le numéro, le montant hors taxes, la TVA et le montant toutes taxes comprises, au format JSON.",
    "languages": ["fr", "en"],
    "restrictions": ["Factures dactylographiées uniquement"]
  },
  "benchmark_manifest": [
    {
      "name": "exemple-factures",
      "version": "1.0",
      "dataset_hash": "7ba9e50d422347a03d484394c30ff88ff3ec11944cc10588a784554326c8d8d2",
      "metric": "exactitude des champs",
      "score": 0.94,
      "baseline_score": 0.71
    }
  ],
  "license": "LicenseRef-PUCIA-Commercial",
  "pricing": {
    "model": "paid",
    "currency": "XOF",
    "amount": 1250000
  },
  "provenance": {
    "method": "masque binaire appris sur la couche 12, poids de base figés",
    "training_data": "12 000 factures synthétiques générées pour l'exemple",
    "data_rights": "données synthétiques, libres de droits"
  },
  "lifecycle": "active",
  "migration": {
    "commitment": true,
    "delay_days": 90
  },
  "safety": {
    "risks": ["erreur d'extraction sur factures manuscrites"],
    "tests": ["banc exemple-factures 1.0", "régression sur banc généraliste"]
  },
  "rollback": {
    "procedure": "désactiver le masque ; le modèle de base reprend son comportement d'origine"
  }
}
```

Signature correspondante (`signatures/manifest.sig`) :

```text
ubTN6xN3hPfbjbxKdotVrn08ZrPmcX0BLtZ7/cNKts26PZFR1VvrHWxJyQNXQrWYeLG+41D6vWdvCv+dsrb7DA==
```

Vérification par l'implémentation de référence :

```text
$ python verify.py exemple-masque-extraction pucia-0001-manifest.schema.json
CONFORME PUCIA-0001 (contrôles V1 à V9)
```

## Annexe B — Références normatives

- RFC 2119 et RFC 8174 : mots-clés d'exigence.
- RFC 8259 : format JSON.
- RFC 8785 : JSON Canonicalization Scheme.
- RFC 8032 : algorithme de signature Ed25519.
- RFC 4648 : encodage base64.
- RFC 3339 : format des dates et heures.
- RFC 3161 : protocole d'horodatage.
- RFC 5646 (BCP 47) : étiquettes de langue.
- RFC 5612 : numéro d'entreprise privée réservé à la documentation.
- RFC 2606 : noms de domaine réservés à la documentation.
- FIPS 180-4 : fonction de hachage SHA-256.
- IEEE 1003.1-2001 (POSIX.1-2001) : format d'archive pax.
- ISO 4217 : codes des monnaies.
- Liste des licences SPDX.
- OpenTimestamps : format de preuve d'horodatage ancré dans la chaîne Bitcoin.
- JSON Schema, version 2020-12.
