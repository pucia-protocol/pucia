# PUCIA — Universal Protocol for the Configuration of Artificial Intelligences

> **Français :** la version de référence de cette page est [`README.md`](https://github.com/pucia-protocol/pucia/blob/main/README.md). This page is its English translation; in case of discrepancy, the French version prevails.

PUCIA is an open protocol that lets artificial intelligences publish, validate, certify and reuse specialised configurations, instead of starting every training run from scratch. A fixed base of parameters, configurations that change everything, knowledge produced once and shared by all.

**Author and principal maintainer:** Honoré DEMBELE
**Registry operator:** Pixel AI SARLU (Abidjan)

## What is in this repository

| File | Role |
|---|---|
| [`PUCIA_Protocole_Universel_pour_IA_v1.5.md`](https://github.com/pucia-protocol/pucia/blob/main/PUCIA_Protocole_Universel_pour_IA_v1.5.md) | White paper, version 1.5 (in French): vision, architecture, hypotheses, experimental plan, economic model, governance. |
| [`PUCIA-0001.md`](https://github.com/pucia-protocol/pucia/blob/main/PUCIA-0001.md) | Standard PUCIA-0001, version 0.1.0 (draft standard, in French): configuration package and manifest format. |
| [`pucia-0001-manifest.schema.json`](https://github.com/pucia-protocol/pucia/blob/main/pucia-0001-manifest.schema.json) | Normative JSON schema of the manifest, an integral part of PUCIA-0001. |
| [`verify.py`](https://github.com/pucia-protocol/pucia/blob/main/verify.py) | Reference verifier: runs checks V1 to V9 of PUCIA-0001. |
| [`exemple-masque-extraction/`](https://github.com/pucia-protocol/pucia/tree/main/exemple-masque-extraction) | Signed example package, declared conformant by the verifier. |
| [`EMPREINTES-SHA256.txt`](https://github.com/pucia-protocol/pucia/blob/main/EMPREINTES-SHA256.txt) | SHA-256 fingerprints of every file in the repository at the date of publication. |
| [`ANTERIORITE.md`](https://github.com/pucia-protocol/pucia/blob/main/ANTERIORITE.md) | How to verify the timestamp proofs of the initial publication (French and English). |
| [`LICENSE`](https://github.com/pucia-protocol/pucia/blob/main/LICENSE) | Apache 2.0 licence, applicable to the code. |
| [`LICENSE-SPEC`](https://github.com/pucia-protocol/pucia/blob/main/LICENSE-SPEC) | Creative Commons Attribution 4.0 International licence, applicable to the specification and the white paper. |
| [`CONTRIBUTING.md`](https://github.com/pucia-protocol/pucia/blob/main/CONTRIBUTING.md) | Contribution rules for humans and AI agents (in French). |
| [`CITATION.cff`](https://github.com/pucia-protocol/pucia/blob/main/CITATION.cff) | How to cite PUCIA. |

## Verify a package

```text
pip install jsonschema cryptography
python verify.py exemple-masque-extraction pucia-0001-manifest.schema.json
```

Expected result:

```text
CONFORME PUCIA-0001 (contrôles V1 à V9)
```

The verifier prints its verdict in French: it means "conformant with PUCIA-0001 (checks V1 to V9)". This result attests the structure of the package, the integrity of its content and the presence of the timestamp proofs. The cryptographic validity of the proofs falls under PUCIA-0002, and the identity of the publisher under PUCIA-0003.

## Signed documents

The white paper v1.5 and the standard PUCIA-0001 were electronically signed on 15 November 2026 by their author, Honoré DEMBELE, using Pixel Sceau (PAdES signature anchored on Bitcoin through OpenTimestamps). The signed PDF versions and their certificates are added to the repository once their anchorings are confirmed.

## Governance

PUCIA is an open project with a single maintainer. Any person and any AI agent may propose a contribution; the automated benches examine it, then the maintainer alone decides whether it enters the standard. See `CONTRIBUTING.md` and sections 7 and 10 of the white paper.

## Licences and name

The code is released under the Apache 2.0 licence; the specification and the white paper under the Creative Commons Attribution 4.0 International licence.

The PUCIA name and the mention "PUCIA certified" belong to their author. Anyone may write that a piece of software is "compatible with the PUCIA specification". Only the registry operator may present itself as such, and only approved validators may issue the mention "PUCIA certified".

## Cite PUCIA

Use the "Cite this repository" button on this page, or the [`CITATION.cff`](https://github.com/pucia-protocol/pucia/blob/main/CITATION.cff) file.
