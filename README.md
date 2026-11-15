# PUCIA — Protocole Universel de Configuration des Intelligences Artificielles

PUCIA est un protocole ouvert qui permet aux intelligences artificielles de publier, valider, certifier et réutiliser des configurations spécialisées, au lieu de recommencer chaque entraînement à zéro. Une base de paramètres fixe, des configurations qui changent tout, un savoir produit une fois et partagé par tous.

**Auteur et mainteneur principal :** Honoré DEMBELE
**Opérateur du registre :** Pixel AI SARLU (Abidjan)

## Contenu du dépôt

| Fichier | Rôle |
|---|---|
| `PUCIA_Protocole_Universel_pour_IA_v1.5.md` | Livre blanc, version 1.5 : vision, architecture, hypothèses, plan expérimental, modèle économique, gouvernance. |
| `PUCIA-0001.md` | Norme PUCIA-0001, version 0.1.0 (projet de norme) : format du paquet de configuration et du manifeste. |
| `pucia-0001-manifest.schema.json` | Schéma JSON normatif du manifeste, partie intégrante de PUCIA-0001. |
| `verify.py` | Vérificateur de référence : exécute les contrôles V1 à V9 de PUCIA-0001. |
| `exemple-masque-extraction/` | Paquet d'exemple signé, déclaré conforme par le vérificateur. |
| `EMPREINTES-SHA256.txt` | Empreintes SHA-256 de tous les fichiers du dépôt à la date de publication. |
| `LICENSE` | Licence Apache 2.0, applicable au code. |
| `LICENSE-SPEC` | Licence Creative Commons Attribution 4.0 International, applicable à la spécification et au livre blanc. |
| `CONTRIBUTING.md` | Règles de contribution pour les humains et les agents IA. |

## Vérifier un paquet

```text
pip install jsonschema cryptography
python verify.py exemple-masque-extraction pucia-0001-manifest.schema.json
```

Résultat attendu :

```text
CONFORME PUCIA-0001 (contrôles V1 à V9)
```

Ce résultat atteste la structure du paquet, l'intégrité de son contenu et la présence des preuves d'horodatage. La validité cryptographique des preuves relève de PUCIA-0002 et l'identité du publieur de PUCIA-0003.

## Documents signés

Le livre blanc v1.5 et la norme PUCIA-0001 ont été signés électroniquement le 15 novembre 2026 par leur auteur, Honoré DEMBELE, au moyen de Pixel Sceau (signature PAdES ancrée sur Bitcoin par OpenTimestamps). Les versions PDF signées et leurs certificats sont ajoutés au dépôt dès la confirmation de leurs ancrages.

## Gouvernance

PUCIA est un projet ouvert à mainteneur unique. Toute personne et tout agent IA peut proposer une contribution ; les bancs automatiques l'examinent, puis le mainteneur décide seul de son intégration au standard. Voir `CONTRIBUTING.md` et les sections 7 et 10 du livre blanc.

## Licences et nom

Le code est diffusé sous licence Apache 2.0 ; la spécification et le livre blanc sous licence Creative Commons Attribution 4.0 International.

Le nom PUCIA et la mention « PUCIA certifié » appartiennent à leur auteur. Chacun peut écrire qu'un logiciel est « compatible avec la spécification PUCIA ». Seul l'opérateur du registre peut se présenter comme tel, et seuls les validateurs agréés peuvent délivrer la mention « PUCIA certifié ».
