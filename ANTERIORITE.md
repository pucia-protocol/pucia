# Antériorité — Anteriority

> **FR.** Ce document atteste l'antériorité de la publication initiale de PUCIA par un
> horodatage [OpenTimestamps](https://opentimestamps.org) ancré dans la blockchain Bitcoin.
> **EN.** This document attests the anteriority of PUCIA's initial release through an
> [OpenTimestamps](https://opentimestamps.org) proof anchored in the Bitcoin blockchain.

---

## FR — Ce qui est prouvé

Le commit de publication initiale de ce dépôt a été horodaté de façon indépendante de
GitHub. La preuve est ancrée dans Bitcoin : elle reste vérifiable même si ce dépôt
disparaissait.

| Élément | Valeur |
|---|---|
| Commit | `8cd17df496002554721419c7a84062193f583197` |
| Date de l'horodatage | 15 novembre 2026 |
| Ancrage Bitcoin (bloc le plus ancien) | **975 880** |
| Fichier horodaté | [`anteriorite/pucia-commit-8cd17df.txt`](anteriorite/pucia-commit-8cd17df.txt) |
| SHA-256 du fichier horodaté | `8ca06bdaf3f36449af2f5c90e9fd80577175b6d9fe2ae0f735fcfe85a964a9cc` |
| Preuve OpenTimestamps | [`anteriorite/pucia-commit-8cd17df.txt.ots`](anteriorite/pucia-commit-8cd17df.txt.ots) |

### Vérifier soi-même

```bash
pip install opentimestamps-client
ots verify anteriorite/pucia-commit-8cd17df.txt.ots
```

La vérification complète lit la blockchain Bitcoin ; avec un nœud Bitcoin local, `ots verify`
confirme le bloc. Sans nœud local, `ots info anteriorite/pucia-commit-8cd17df.txt.ots` affiche
les attestations de blocs confirmés.

> L'intégrité des fichiers publiés est par ailleurs attestée par
> [`EMPREINTES-SHA256.txt`](EMPREINTES-SHA256.txt) :
> `sha256sum -c EMPREINTES-SHA256.txt` doit répondre `OK` sur chaque ligne.

### Preuves par document

Au-delà du commit, chaque document signé est horodaté **séparément** sur sa propre
empreinte. La preuve `.ots` est placée à côté du document ; pour la vérifier :
`ots verify <document>.ots`.

| Document | SHA-256 | Preuve |
|---|---|---|
| Livre blanc v1.5 | `abc86f983af6a1c7b1145f3ae94897966f7f008789e16c9aa018f718cc60dfbd` | [`PUCIA_Protocole_Universel_pour_IA_v1.5.md.ots`](PUCIA_Protocole_Universel_pour_IA_v1.5.md.ots) |
| Norme PUCIA-0001 | `7922a5bf96ec6b8094681febf36e6ec7dc1985037ed660fd93a862f218b3ba1f` | [`PUCIA-0001.md.ots`](PUCIA-0001.md.ots) |

Ces deux preuves sont ancrées dans Bitcoin depuis le 15 novembre 2026 (bloc le plus ancien : **975 934**).

---

## EN — What is proven

The initial-release commit of this repository was timestamped independently of GitHub. The
proof is anchored in Bitcoin and remains verifiable even if this repository were to disappear.

| Item | Value |
|---|---|
| Commit | `8cd17df496002554721419c7a84062193f583197` |
| Timestamp date | 15 November 2026 |
| Bitcoin anchor (earliest block) | **975,880** |
| Timestamped file | [`anteriorite/pucia-commit-8cd17df.txt`](anteriorite/pucia-commit-8cd17df.txt) |
| SHA-256 of timestamped file | `8ca06bdaf3f36449af2f5c90e9fd80577175b6d9fe2ae0f735fcfe85a964a9cc` |
| OpenTimestamps proof | [`anteriorite/pucia-commit-8cd17df.txt.ots`](anteriorite/pucia-commit-8cd17df.txt.ots) |

### Verify it yourself

```bash
pip install opentimestamps-client
ots verify anteriorite/pucia-commit-8cd17df.txt.ots
```

Full verification reads the Bitcoin blockchain; with a local Bitcoin node, `ots verify`
confirms the block. Without one, `ots info anteriorite/pucia-commit-8cd17df.txt.ots` prints the
confirmed block attestations.

> File integrity is additionally attested by [`EMPREINTES-SHA256.txt`](EMPREINTES-SHA256.txt):
> `sha256sum -c EMPREINTES-SHA256.txt` must return `OK` on every line.

### Per-document proofs

Beyond the commit, each signed document is timestamped **separately** on its own
digest. The `.ots` proof sits next to its document; to verify:
`ots verify <document>.ots`.

| Document | SHA-256 | Proof |
|---|---|---|
| White paper v1.5 | `abc86f983af6a1c7b1145f3ae94897966f7f008789e16c9aa018f718cc60dfbd` | [`PUCIA_Protocole_Universel_pour_IA_v1.5.md.ots`](PUCIA_Protocole_Universel_pour_IA_v1.5.md.ots) |
| PUCIA-0001 norm | `7922a5bf96ec6b8094681febf36e6ec7dc1985037ed660fd93a862f218b3ba1f` | [`PUCIA-0001.md.ots`](PUCIA-0001.md.ots) |

Both proofs have been anchored in Bitcoin since 15 November 2026 (oldest block: **975 934**).
