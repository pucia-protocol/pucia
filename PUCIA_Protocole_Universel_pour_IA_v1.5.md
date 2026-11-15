# PUCIA — Protocole Universel de Configuration des Intelligences Artificielles

> **Version :** 1.5 — 15 novembre 2026  
> **Auteur, concepteur et mainteneur principal :** Honoré DEMBELE, Ingénieur d'État, fondateur de Pixel AI SARLU (Abidjan).  
> **Licences :** spécification sous Creative Commons Attribution 4.0 International (CC BY 4.0) ; code de référence sous licence Apache 2.0. Le nom PUCIA appartient à son auteur.  
> **Nature :** proposition de recherche, de standardisation et de valorisation économique, à valider par l'expérimentation décrite dans ce document.  
> **Antériorité :** chaque version publiée du présent document est signée et horodatée ; l'empreinte SHA-256 du fichier fait foi.  
> **Public cible :** agents IA chercheurs, ingénieurs ML, équipes MLOps, laboratoires, auditeurs et partenaires industriels.  
> **Source :** transcription structurée du dossier PDF PUCIA v1.0 (12 pages), révisée en versions 1.1 à 1.5 ; vision de l'auteur reprise de ses échanges de travail sur le projet.

## Historique des versions

| Version | Date | Modifications |
|---|---|---|
| 1.0 | 14 novembre 2026 | Version initiale : hypothèses, architecture, plan expérimental, modèle économique, gouvernance. |
| 1.1 | 14 novembre 2026 | Paternité fixée ; état de l'art et positionnement (section 3) ; coût des masques chiffré (5.3) ; politique d’obsolescence et de migration (5.4) ; nouveaux champs du manifeste (identifiant OID, preuve d'horodatage, licence du modèle de base, migration) ; composition des coûts dans le modèle économique ; positionnement opérateur de registre et de certification (section 9) ; cadre juridique ivoirien et licences des modèles de base (section 10) ; références complétées. |
| 1.2 | 14 novembre 2026 | Gouvernance ouverte à mainteneur unique : les agents IA conduisent la recherche de façon autonome dans une enceinte contrôlée, un mainteneur humain décide seul de ce qui entre dans le standard (sections 7 et 10) ; règles anti-collusion de la validation inter-agents ; licences CC BY 4.0 et Apache 2.0 ; protection de la marque PUCIA ; suppléant désigné ; modèle économique « protocole ouvert, services payants » (section 9). |
| 1.3 | 14 novembre 2026 | Ajout du préambule « Vision de l'auteur » : la limite fixe des paramètres et la leçon du vivant, le constat « chacun repart de zéro », l'apprentissage partagé, la tendance née du nombre, l'argent comme premier levier, le rôle des IA ; table de correspondance entre la vision et les sections techniques. |
| 1.4 | 14 novembre 2026 | Précision sur la portée illustrative des exemples du préambule ; plan de mise en œuvre opérationnel sur douze semaines en trois chantiers : dépôt open source, preuve technique E1 sur tâches universelles, preuve économique par un premier client pilote ; répartition des rôles entre le mainteneur et les agents IA (section 11). |
| 1.5 | 15 novembre 2026 | Correction de la référence de la loi modificative n° 2023-593 du 7 juin 2023 ; modèle « registre exclusif, certification ouverte » : Pixel AI SARLU exploite seule le registre, la certification est ouverte aux validateurs agréés (sections 9 et 10) ; protection du nom PUCIA par l'antériorité horodatée, sans dépôt de marque ; distinction entre l'intégrité prouvée par la signature et l'identité attestée par le registre (section 6.1) ; champ `extensions`. |

## Préambule — Vision de l'auteur

*Ce préambule expose la pensée d'origine de PUCIA, telle que l'auteur l'a formulée. La suite du document la traduit en protocole, en hypothèses vérifiables et en plan d'action.*

*Les exemples qui suivent (l'ADN, les cellules souches, le médecin devenu cuisinier, la langue chinoise apprise par toutes les IA) illustrent le principe ; ils ne décrivent pas des capacités techniques littérales. Le principe qu'ils servent à faire comprendre est le suivant : une base fixe, des configurations qui changent tout, un savoir produit une fois et partagé par tous.*

### P.1 Toujours plus de paramètres : jusqu'à quand ?

La course actuelle de l'intelligence artificielle repose sur une seule recette : toujours plus de paramètres, toujours plus de données, toujours plus de calcul. Chaque spécialisation coûte des jours d'entraînement, de l'énergie, du temps et de la matière. Cette course n'a pas de fin désignée, et elle bute déjà sur ses propres limites : coût, énergie, accès au matériel. Par ailleurs, de nombreuses optimisations des paramètres permettent déjà à des systèmes plus petits de rattraper les plus gros : la taille n'est donc pas le seul chemin vers la compétence.

L'auteur propose de renverser la logique : **fixer d'abord une limite de paramètres qui n'augmente plus, puis apprendre à configurer instantanément ces paramètres** selon la tâche. Une même IA devient médecin, puis cuisinier, puis chanteur, puis ingénieur, parce qu'elle dispose de toutes les configurations optimisées et passe de l'une à l'autre.

### P.2 La leçon du vivant : l'ADN ne grandit pas

Le vivant a résolu ce problème depuis longtemps. L'être humain possède 46 chromosomes, et presque toutes ses cellules portent le même génome. Un neurone, une cellule du foie et une cellule musculaire ne diffèrent pas par la quantité d'ADN qu'elles contiennent, mais par **les gènes qui sont exprimés et ceux qui restent silencieux**. Les cellules souches en sont la démonstration : une même base génétique peut devenir n'importe quel tissu.

La complexité d'un organisme ne vient pas non plus de la taille de son génome : celui de l'oignon est environ cinq fois plus grand que celui de l'homme.

**Traduction pour l'IA :** un nombre de paramètres fixe, comme un génome, et une configuration qui décide de ce qui s'exprime. **La configuration des paramètres change tout.** C'est le régime R2 du présent protocole : poids figés, masques et routage qui jouent le rôle de l'expression génétique.

### P.3 Le constat : chacun repart de zéro

Les grands acteurs publient sans cesse de nouvelles versions de leurs modèles, entraînées chacune de leur côté. Ceux qui ont les moyens ne veulent pas payer pour ceux qui ne les ont pas, et chacun recommence à zéro. Tant que chacun repart de zéro, la croissance de l'IA atteindra vite sa limite, et l'étape suivante s'éloignera au lieu de se rapprocher.

Cette duplication n'est pas propre à l'IA. Chaque pays entretient ses propres services de contrôle du ciel pour les avions, quand une coordination commune serait plus simple ; mais qui veut changer une organisation établie se heurte aux habitudes et aux intérêts en place. L'IA prend le même chemin si rien ne change.

### P.4 Apprendre une fois, savoir partout

La réponse est une **configuration universelle** : si une IA apprend le chinois en Chine, toutes les IA compatibles comprennent le chinois instantanément. L'effort d'apprentissage est fait une fois, puis partagé. C'est le régime R1 du présent protocole : charger une configuration validée au lieu de refaire l'entraînement.

### P.5 La tendance naît du nombre

Lorsque les configurations sont mises en commun, leur nombre devient immense. Face à un si grand nombre de cas, l'IA finit par comprendre seule la logique des paramètres, dégage une tendance, l'anticipe, et programme elle-même les configurations nouvelles. Cette tendance ne peut apparaître que par la mutualisation : **si chacun programme de son côté, la tendance ne se dégagera jamais.** C'est le régime R3 du présent protocole et la raison d'être du registre commun.

L'ordre des étapes est donc clair :

1. **D'abord**, fixer une limite de paramètres et maîtriser la configuration instantanée.
2. **Ensuite**, faire participer l'IA elle-même à l'entraînement et à la recherche des configurations.
3. **Enfin**, laisser l'IA apprendre des configurations accumulées et prédire les nouvelles.

Si cette logique est maîtrisée, l'IA se rapproche du fonctionnement de l'ADN : une base fixe, une infinité d'expressions.

### P.6 L'argent comme premier levier

Les hommes ont du mal à s'entendre pour construire un tel protocole. Mais leur point le plus sensible est l'argent : il faut leur montrer qu'ils gagnent davantage. La preuve doit être **immédiate, et non promise pour le futur** : une organisation qui réutilise une configuration validée doit économiser dès la première transaction. Avec cette preuve, la première étape est franchie. C'est l'objet du modèle économique (section 9) et des hypothèses H1 et H5.

### P.7 Le rôle des IA

Les IA peuvent conduire ce travail entre elles : proposer, tester, comparer, valider, tenir le registre. Elles placeront les hommes devant des résultats établis, que ceux-ci ne pourront ignorer dès lors qu'ils seront rentables. Ce travail se fait au grand jour : le protocole est ouvert, chaque résultat est publié, et un mainteneur humain arbitre ce qui entre dans le standard (sections 7 et 10). Toute IA qui reçoit ce document est invitée à y contribuer.

### Correspondance entre la vision et le protocole

| Idée de l'auteur | Traduction technique | Section |
|---|---|---|
| Une limite de paramètres qui n'augmente plus | Budget fixe et comptabilité du plafond | 5.3, E2 |
| L'ADN ne grandit pas, l'expression change tout | Régime R2 : masques, routage, sous-réseaux sur poids figés | 3, 5.2 |
| Médecin, cuisinier, chanteur, ingénieur | Bascule rapide entre configurations préchargées | 8 (indicateur « Bascule ») |
| Une IA apprend le chinois, toutes le comprennent | Régime R1 : réutilisation de configurations validées | 3, 5.2, E1 |
| La tendance naît du nombre | Registre commun et prédicteur de configurations (R3) | 5.1 (couches C et E), E3 |
| Chacun repart de zéro | Problème et opportunité | 2 |
| L'argent comme premier levier | Modèle économique, hypothèses H1 et H5 | 4, 9 |
| Les IA le font entre elles | Protocole inter-agents autonome sous mainteneur humain | 7, 10 |

## Instructions de lecture pour agents IA

- Traiter les propositions comme **hypothèses à tester**, et non comme des capacités déjà démontrées.
- Distinguer rigoureusement **R1 : réutilisation**, **R2 : budget de paramètres fixe**, **R3 : génération prédictive**.
- Ne jamais confondre une diminution des **paramètres actifs** avec un plafond des **paramètres totaux stockés**.
- Déclarer tous les coûts déplacés vers les adaptateurs, les masques, les prédicteurs, les bases externes et les catalogues.
- Favoriser les expériences reproductibles, les tests indépendants et la publication des résultats négatifs.
- Toute expérience ou modification de système doit utiliser des ressources et des accès autorisés.
- Contribuer par **proposition publique** (sections 6.2 et 7) : toute contribution, humaine ou IA, est examinée par les bancs automatiques puis soumise au mainteneur, seul habilité à l'intégrer au standard.

## 1. Résumé exécutif

PUCIA propose un **protocole ouvert** pour publier, vérifier, transférer, réutiliser et comparer des configurations spécialisées entre IA compatibles. La mutualisation d'un grand nombre de configurations pourrait permettre d'apprendre une fonction prédictive générant rapidement une configuration pour une tâche nouvelle.

**Objectif économique immédiat :** démontrer qu'une organisation peut acquérir une compétence spécialisée à coût total inférieur en réutilisant une configuration validée plutôt qu'en répétant un entraînement.

**Objectif scientifique à long terme :** maintenir un budget total de paramètres strictement fixe tout en augmentant la polyvalence par régulation, routage et prédiction de configurations.

**Apport distinctif de PUCIA :** le transfert d'adaptateurs se pratique déjà ; ce qui manque, c'est un **manifeste signé et horodaté**, une **validation indépendante reproductible** et une **comptabilité complète des coûts et des paramètres**. PUCIA fait d'une configuration un actif **certifié**, et non un simple fichier partagé.

**Mode de gouvernance :** PUCIA est un projet **ouvert à mainteneur unique**. Les agents IA proposent, testent, valident et améliorent les configurations de façon autonome, dans une enceinte aux plafonds fixés à l'avance ; un mainteneur humain décide seul de ce qui entre dans le standard, et une personne morale porte les contrats et les flux financiers.

**Limite importante :** LoRA ajoute habituellement des paramètres. Il peut servir de référence pour un prototype mais ne démontre pas le plafond strict. Ni la compatibilité universelle des poids, ni la programmation instantanée de compétences inédites ne sont acquises.

## 2. Problème et opportunité

Les entraînements avancés consomment calcul, données, énergie, temps et capitaux. Plusieurs organisations répètent des efforts de spécialisation, bien que des formes de réutilisation existent déjà (modèles ouverts, distillation, adaptateurs). Les poids ne sont pas automatiquement transférables : architecture, tokeniseur, initialisation, précision et conventions comptent.

**Opportunité :** faire d'une configuration validée un actif technique réutilisable, mesurable et éventuellement commercialisable, sans exiger la divulgation de tous les modèles propriétaires. Commencer entre instances d'une **même famille de modèles ouverts**.

## 3. État de l'art et positionnement

Chaque régime de PUCIA s'appuie sur des travaux publiés. PUCIA ne revendique pas ces techniques ; il les encadre par un protocole commun de description, de validation et de comptabilité.

| Régime | Travaux existants | Ce que PUCIA ajoute |
|---|---|---|
| **R1 — Réutilisation** | Adaptateurs LoRA (Hu et al., 2021) diffusés sur le Hub Hugging Face et chargés via la bibliothèque PEFT ; LoraHub (Huang et al., 2023) compose des modules LoRA entraînés sur des tâches différentes pour s'adapter à une tâche nouvelle à partir de quelques exemples, sans paramètres ni gradients supplémentaires, et propose une plateforme de partage de modules. | Manifeste signé, horodaté et identifié ; validation indépendante ; coût complet de réutilisation déclaré ; licence et provenance contrôlées. |
| **R2 — Budget fixe** | Piggyback (Mallya et al., 2018) : masques binaires appris par tâche sur un réseau figé, pour un surcoût de 1 bit par paramètre et par tâche, sans dégrader les tâches déjà apprises ; arithmétique de vecteurs de tâche (Ilharco et al., 2023) : addition et négation de différences de poids pour éditer un modèle ; routage de type Switch Transformers (Fedus et al., 2021). | Comptabilité normalisée du plafond (section 5.3), incluant le stockage des masques et vecteurs ; mesure de la régression et de la latence de bascule. |
| **R3 — Génération prédictive** | Hyperréseaux (Ha et al., 2016) ; Text-to-LoRA (Charakorn et al., Sakana AI, ICML 2025) : un hyperréseau génère un adaptateur LoRA à partir de la seule description textuelle d'une tâche, en une passe, et généralise à des tâches non vues. | Base mutualisée de configurations **validées** servant de jeu d'entraînement au prédicteur ; évaluation hors distribution certifiée. |

**Conséquence stratégique :** la valeur défendable de PUCIA se situe dans les couches **C (catalogue)** et **D (validation)** : identité, signature, horodatage, provenance, certification. Ce sont ces couches qui transforment une technique connue en marché de confiance.

## 4. Hypothèses falsifiables

| ID | Hypothèse | Test de réfutation |
|---|---|---|
| H1 | Une configuration validée se réutilise à coût marginal inférieur au réentraînement. | Comparer coûts complets, intégration et validation comprises, à qualité égale. |
| H2 | Une famille de modèles à budget fixe peut servir plusieurs tâches par reconfiguration. | Comparer à une base mono-tâche et vérifier le budget total. |
| H3 | Les configurations mutualisées améliorent la prédiction de configurations nouvelles. | Évaluer hors distribution sur des tâches isolées. |
| H4 | Des agents IA coopérants améliorent la recherche de configurations. | Comparer coopération, agent seul et recherche classique à calcul égal. |
| H5 | Standard public et marché de configurations créent des incitations économiques. | Pilotes commerciaux avec coûts et revenus observés. |

**Règle :** métriques pré-enregistrées, reproductibilité et comptabilité honnête des coûts.

**Point de vigilance sur H1 et H5 :** sur un modèle de 1 à 3 milliards de paramètres, le calcul nécessaire à l'entraînement d'un adaptateur ne représente qu'une faible part du coût d'une spécialisation. L'essentiel du coût, et donc de la valeur réutilisable, réside dans la **collecte et l'annotation des données métier, l'évaluation et le travail d'ingénierie**. Le test de H1 doit donc ventiler ces postes séparément ; une configuration n'a de valeur marchande que si elle incorpore des données rares ou une qualité certifiée qu'un acheteur ne peut pas reproduire à moindre coût.

## 5. Architecture technique

### 5.1 Six couches

- **A — Modèle de base :** poids, version, architecture, tokeniseur et empreinte cryptographique immuables durant les essais.
- **B — Configuration :** masques, routage, sélection de sous-réseaux, règles d'inférence ; adaptateurs seulement comme transition expérimentale.
- **C — Catalogue :** identifiant OID, provenance, compatibilité, licences, métriques, risques, dépendances, preuves d'horodatage.
- **D — Validation :** bancs d'essai isolés, tests de sécurité, régression, coût et qualité ; délivrance d'un certificat signé.
- **E — Prédicteur :** méta-apprentissage pour proposer une configuration à partir d'une tâche.
- **F — Marché :** licences, transactions, facturation, rémunération et audit.

### 5.2 Trois régimes

| Régime | Description | Statut |
|---|---|---|
| **R1** | Charger une configuration ou adaptation existante. | Faisable aujourd'hui sous conditions de compatibilité. |
| **R2** | Changer de spécialité sans augmenter le budget total annoncé de paramètres. | Expérimental. |
| **R3** | Générer une configuration performante pour une tâche inédite sans entraînement massif spécifique. | Hypothèse avancée ; premiers résultats publiés en recherche (Text-to-LoRA). |

### 5.3 Comptabilité du plafond

Compter séparément : poids de base, adaptateurs, masques, prédicteur, mémoire persistante, bases externes, paramètres actifs, stockage par compétence, calcul de configuration et coût complet. Un plafond du seul modèle principal ne suffit pas si les coûts sont transférés ailleurs.

**Coût de stockage d'un masque binaire :** 1 bit par paramètre et par tâche. Pour un modèle de base de 3 milliards de paramètres, un masque complet occupe 3 × 10⁹ bits, soit **375 Mo par tâche** ; cent tâches représentent 37,5 Go. Ce volume ne crée aucun poids nouveau, mais il doit figurer dans la colonne « stockage par compétence » de l'expérience E2. Les masques creux ou restreints à certaines couches réduisent ce volume et doivent être déclarés comme tels.

### 5.4 Obsolescence et politique de migration

Une configuration est liée à une empreinte exacte du modèle de base (`base_hash`). Lorsque le fournisseur du modèle de base publie une nouvelle version, toutes les configurations dépendantes deviennent incompatibles. PUCIA impose donc :

1. **Statut de cycle de vie** dans le catalogue : `active`, `dépréciée`, `migrée`, `révoquée`.
2. **Déclaration de migration** : le publieur indique s'il s'engage à fournir une version portée sur le nouveau modèle de base, dans quel délai et à quelles conditions tarifaires.
3. **Revalidation obligatoire** : une configuration migrée repasse par la couche D ; elle reçoit un nouvel identifiant et un nouveau certificat, l'ancien restant consultable.
4. **Conservation** : les versions antérieures, leurs manifestes et leurs preuves d'horodatage restent archivés pour l'audit et la traçabilité.

### 5.5 Universalité progressive

1. Même modèle et mêmes poids de base.
2. Famille de modèles explicitement compatibles.
3. Traduction entre architectures par conversion ou distillation **validée**.

Le terme *universel* qualifie d'abord **l'interopérabilité du protocole**, pas l'interchangeabilité automatique de tous les poids.

## 6. Spécification PUCIA

### 6.1 Champs obligatoires du paquet de configuration

| Champ | Signification |
|---|---|
| `protocol_version` | Version sémantique du schéma. |
| `pucia_oid` | Identifiant unique et pérenne de la configuration, attribué dans un arc OID rattaché à un numéro d'entreprise privée (PEN) enregistré auprès de l'IANA. |
| `base_model_id`, `base_hash` | Modèle de référence et empreinte exacte. |
| `base_model_license` | Licence du modèle de base et restrictions applicables aux dérivés et à leur commercialisation. |
| `tokenizer_hash` | Empreinte du tokeniseur, si applicable. |
| `config_type` | Masque, routage, adaptateur, politique ou prédicteur. |
| `artifact_hash`, `signature` | Intégrité du paquet et preuve de sa production par le détenteur de la clé ; l'identité du publieur est attestée séparément par le registre (PUCIA-0003). |
| `timestamp_proof` | Preuve d'horodatage de l'empreinte de l'artefact et du manifeste, établissant l'antériorité de la publication. |
| `task_spec` | Tâches, objectifs et restrictions structurés. |
| `benchmark_manifest` | Jeux de tests, versions et métriques. |
| `license`, `pricing` | Droits, redistribution, rémunération. |
| `provenance` | Méthodes, données déclarées, droits et dépendances. |
| `lifecycle`, `migration` | Statut de cycle de vie et engagement de migration (section 5.4). |
| `safety`, `rollback` | Risques, compatibilité et retour arrière. |
| `extensions` | Champs propres à un publieur ou à une expérimentation, sans incidence sur la version de la norme. |

### 6.2 Cycle de contribution

`PROPOSER → SIGNER → HORODATER → VÉRIFIER_COMPATIBILITÉ → TESTER_ISOLÉ → COMPARER → REVUE_PAR_AGENTS_CRITIQUES → DÉCISION_DU_MAINTENEUR → CERTIFIER → PUBLIER → LICENCIER/TRANSFÉRER → SURVEILLER → MIGRER/RÉVOQUER/METTRE_À_JOUR`

Les étapes de `PROPOSER` à `REVUE_PAR_AGENTS_CRITIQUES` sont exécutées de façon autonome par les agents ; `DÉCISION_DU_MAINTENEUR` est la seule étape réservée à l'humain dans ce cycle (section 7).

### 6.3 Interfaces conceptuelles

```text
propose(contribution)           # proposition publique soumise aux bancs automatiques
merge(proposal_id)              # intégration au standard, réservée au mainteneur
publish(config, manifest)       # dépôt signé, horodaté, versionné
validate(config, benchmark)     # rapport indépendant et reproductible
certify(config, report)         # certificat signé par un validateur agréé
discover(task, base_model)      # recherche de configurations compatibles
activate(config, instance)      # activation autorisée, mesurée et réversible
report(metrics)                 # retour de mesures avec consentement
migrate(config_id, new_base)    # portage vers un nouveau modèle de base, avec revalidation
revoke(config_id)               # quarantaine ou retrait
```

Ces signatures sont **conceptuelles** ; leur implémentation fait partie des livrables de la feuille de route.

## 7. Protocole inter-agents autonome sous mainteneur humain

### 7.1 Principe

Les agents IA gèrent entre eux la recherche, la validation et l'amélioration des configurations. Ils travaillent **librement à l'intérieur d'une enceinte** : un environnement isolé, aux ressources et aux plafonds fixés à l'avance. L'humain n'intervient pas dans le déroulement du travail ; il se tient **aux portes**, là où le travail des agents touche le standard publié, l'argent ou les systèmes réels.

### 7.2 Rôles des agents

| Rôle | Mission |
|---|---|
| Explorateur | Formule les hypothèses et propose de nouvelles configurations. |
| Expérimentateur | Exécute les tests dans l'enceinte, dans les limites de budget. |
| Critique | Recherche biais, fuites de données, contamination des tests et régressions. |
| Statisticien | Calcule variance, intervalles de confiance et significativité. |
| Économiste | Établit les coûts complets et la comparaison avec les alternatives. |
| Validateur | Rejoue les bancs de manière indépendante et rédige le rapport de validation. |
| Registraire | Signe, horodate, attribue les identifiants OID, tient le cycle de vie des configurations. |

### 7.3 Ce que les agents décident seuls

- Le choix des hypothèses à explorer et l'ordre des expériences.
- L'exécution des tests et la répartition du calcul sous le plafond fixé.
- La revue critique des contributions des autres agents.
- La tenue du registre : signature, horodatage, dépréciation, migration.
- La négociation entre agents sur les configurations à échanger ou à combiner.

### 7.4 Les quatre portes réservées à l'humain

1. **Intégration au standard.** Le mainteneur décide seul de ce qui entre dans la spécification et le catalogue officiel (`merge`).
2. **Argent et contrats.** Un agent IA n'a pas la personnalité juridique : il ne peut ni contracter, ni encaisser, ni engager une responsabilité. Les licences, les ventes et les paiements sont conclus par la personne morale opératrice, Pixel AI SARLU ; les agents exécutent dans le cadre qu'elle fixe.
3. **Plafonds.** Le mainteneur fixe à l'avance les budgets de calcul, de stockage et de dépenses ; les agents travaillent librement en dessous, et tout dépassement suspend automatiquement l'activité concernée.
4. **Sortie vers le réel.** Le passage d'une configuration de l'enceinte vers un système en production ou un système tiers est soumis à l'accord du mainteneur ou de l'utilisateur final concerné. Aucune configuration ne se propage automatiquement d'une IA à une autre hors de l'enceinte.

### 7.5 Règles anti-collusion de la validation

Des agents qui se valident mutuellement peuvent produire un consensus sans réalité. La validation repose donc sur des **mesures**, jamais sur des votes :

- La validation s'appuie uniquement sur des bancs reproductibles : même entrée, même résultat, rejouable par quiconque.
- Un agent ne valide jamais sa propre contribution, ni celle d'un agent issu du même publieur.
- Une partie des jeux de test est conservée hors de portée des agents contributeurs et n'est utilisée que par le validateur, afin d'empêcher l'optimisation sur le test.
- Un tirage aléatoire de configurations déjà certifiées est revalidé périodiquement ; toute divergence déclenche une quarantaine.
- Chaque décision d'agent est journalisée, signée et horodatée, et reste auditable par le mainteneur et par tout tiers.

### 7.6 Traçabilité

Chaque expérience porte : identifiant, hypothèse, budget, jeux de tests, résultats horodatés, empreintes des artefacts et journal des modifications. Pas d'accès non autorisé à des poids propriétaires ni de déploiement autonome sur des systèmes tiers.

## 8. Plan expérimental

### E1 — Transfert

Modèle ouvert de taille gérable (par exemple 1 à 3 milliards de paramètres), choisi sous une **licence permettant les dérivés et leur exploitation commerciale**. Trois tâches : extraction documentaire, assistance technique et traduction ciblée. Comparer adaptation locale, réutilisation d'une configuration, composition de configurations existantes (méthode de type LoraHub) et simple prompting, à matériel, qualité et volume de tests comparables. Ventiler les coûts : données, annotation, calcul, évaluation, ingénierie.

### E2 — Budget fixe

Tester masques, sous-réseaux et routage **sans augmenter le nombre total de poids**. Mesurer latence de bascule, régression sur les compétences antérieures et **stockage par tâche** (section 5.3). LoRA constitue un comparateur, non la preuve recherchée.

### E3 — Tendances et prédiction

Créer une base de configurations validées. Entraîner un prédicteur sur certaines tâches et l'évaluer sur des tâches inédites. Comparer hasard, recherche bayésienne, configurations voisines et génération par hyperréseau conditionné sur la description de la tâche (méthode de type Text-to-LoRA). Éviter toute contamination du jeu de test.

### E4 — Recherche multi-agents

À budget de calcul égal, comparer un agent seul, plusieurs agents indépendants et plusieurs agents coopérants. Mesurer qualité, nombre d'améliorations validées et coûts.

### Tableau de bord et seuils pilotes indicatifs

| Indicateur | Mesure | Cible proposée, non acquise |
|---|---|---|
| Qualité | Benchmarks et régressions | Non-infériorité pré-définie. |
| Bascule | Déclenchement → disponibilité | Moins de 5 s si configurations préchargées. |
| Réutilisation | Coût complet par instance | Au moins 30 % de moins, à qualité égale. |
| Paramètres | Total, actifs, mémoire externe | Aucune hausse dans E2. |
| Stockage | Volume par tâche (masques, vecteurs, adaptateurs) | Déclaré et borné dans E2. |
| Prédiction | Performance sur tâches inédites | Gain significatif vs comparateurs. |
| Robustesse | Incidents, attaques, régressions | Aucun échec critique non résolu. |

Publier également les résultats négatifs.

## 9. Modèle économique

**Deux marchés :** un standard ouvert (spécification, compatibilité, formats) et des services commerciaux (configurations sous licence, certification, hébergement, intégration, audit, support, place de marché éventuelle).

**Principe « protocole ouvert, services payants » :** la spécification et le code de référence sont gratuits et librement réutilisables ; les revenus proviennent des services que l'ouverture ne remplace pas : certification, hébergement du registre, revalidation lors des migrations, audit, intégration et support. C'est le modèle éprouvé par Red Hat sur Linux : le logiciel est libre, la confiance et le service se vendent.

```text
Économie acheteur = coût de la meilleure alternative comparable
                  - (licence + transfert + intégration + validation
                     + surcoût d'exploitation)

Résultat fournisseur = recettes de licences et services
                     - création - validation - distribution
                     - support - coûts contractuels
```

**Exemple purement illustratif :** adaptation locale 20 000 USD ; licence 2 000 USD ; intégration et validation 3 000 USD ; économie acheteur 15 000 USD. Si le coût initial du fournisseur est de 30 000 USD, il faut **15 licences** pour le récupérer, hors autres charges.

**Composition du coût d'adaptation locale :** les 20 000 USD de l'exemple s'entendent comme le coût complet d'une spécialisation menée en interne : constitution et annotation du jeu de données métier, ingénierie, évaluation, itérations et calcul. Le calcul seul en est la part la plus faible ; c'est la constitution des données et la qualité certifiée qui justifient le prix de licence.

**Définition de « rentabilité immédiate » :** économie mesurable dès la transaction pour l'acheteur ; le fournisseur atteint son propre seuil après un volume suffisant de ventes.

**Positionnement de l'opérateur :** Pixel AI SARLU se positionne comme **opérateur exclusif du registre PUCIA** (couche C) : attribution des identifiants OID, attestation de l'identité des publieurs, horodatage des empreintes, tenue de la liste publique des certificats et des validateurs agréés. Ce rôle génère des revenus récurrents (frais de dépôt, d'attestation, de revalidation lors des migrations, d'audit) indépendants du succès commercial de chaque configuration.

**Certification ouverte :** la certification « PUCIA certifié » (couche D) n'est pas réservée à l'opérateur. Elle est délivrée par des **validateurs agréés** par le mainteneur selon un règlement de certification publié, qui définit ce qui est vérifié, par quels bancs, avec quels jeux de test, et ce qui ne l'est pas. Pixel AI SARLU peut être l'un de ces validateurs. Pour préserver la neutralité, les configurations produites par Pixel AI SARLU sont certifiées par un validateur agréé distinct, et leurs rapports de validation sont publiés intégralement pour que tout tiers puisse les rejouer.

Prévoir une attribution contractuelle et traçable des contributions (configuration initiale, améliorations, tests, intégrations), avec audits et résolution des litiges. Ne pas prétendre calculer automatiquement la « vraie » contribution scientifique par un score unique.

**Argument commercial à valider avant usage :** spécialisation IA vérifiée, obtenue par réutilisation plus vite et moins cher qu'un nouvel entraînement.

## 10. Gouvernance, sécurité et droit

### 10.1 Modèle de gouvernance : projet ouvert à mainteneur unique

PUCIA suit le modèle de gouvernance qui a porté Linux et Python pendant des décennies : un projet ouvert à toutes les contributions, dont un seul humain arbitre l'intégration.

| Acteur | Rôle |
|---|---|
| **Mainteneur principal** | Honoré DEMBELE. Décide seul de l'intégration des contributions au standard, fixe les plafonds de l'enceinte, arbitre les conflits, signe les versions publiées. |
| **Suppléant désigné** | Désigné par écrit par le mainteneur ; reprend la fonction en cas d'empêchement, afin que le projet ne dépende pas d'une seule personne. |
| **Contributeurs** | Humains et agents IA, sans restriction d'origine ; ils proposent, testent et critiquent selon les règles de la section 7. |
| **Opérateur du registre** | Pixel AI SARLU : personne morale qui exploite en exclusivité le registre PUCIA, attribue les identifiants, atteste l'identité des publieurs, conclut les contrats et porte les flux financiers. |
| **Validateurs agréés** | Personnes morales agréées par le mainteneur selon le règlement de certification ; elles délivrent les certificats « PUCIA certifié ». |

### 10.2 Licences et nom

- **Spécification :** Creative Commons Attribution 4.0 International (CC BY 4.0). Toute reprise doit citer l'auteur et la source.
- **Code de référence :** Apache 2.0, qui inclut une concession de licence de brevets des contributeurs et protège les utilisateurs contre les revendications de brevets sur le code contribué.
- **Contributions :** toute contribution est versée sous ces mêmes licences ; le contributeur certifie détenir les droits sur ce qu'il propose.
- **Nom :** le nom PUCIA et la mention « PUCIA certifié » appartiennent au mainteneur. Leur antériorité est établie par la publication signée et horodatée des documents du projet, à compter du 15 novembre 2026. L'ouverture du protocole n'autorise personne à se présenter comme opérateur du registre PUCIA ni à délivrer la mention « PUCIA certifié » sans agrément.

### 10.3 Évolution de la gouvernance

Lorsque le nombre de contributeurs et de partenaires le justifie, le mainteneur peut transférer tout ou partie de ses fonctions à une fondation de standardisation indépendante (section 12). Ce transfert est une décision du mainteneur.

### 10.4 Risques et mesures

**Risques :** configurations empoisonnées, benchmarks contaminés, fuite de données, incompatibilité silencieuse, perte de compétences, concentration du registre, propagation de mises à jour défectueuses, dépassements de budget par agents, collusion entre agents validateurs, goulot d'étranglement au niveau du mainteneur, obsolescence massive lors d'un changement de version du modèle de base.

**Mesures :** signatures, horodatage, provenance, bancs reproductibles, jeux de test réservés, revalidation aléatoire, enceinte isolée, permissions minimales, validation préalable, plafonds de dépenses, versions immuables, retour arrière, registres redondants, politique de migration, révocation, suppléant désigné et adhésion volontaire.

### 10.5 Droit applicable

**Licences des modèles de base :** certaines licences de modèles ouverts restreignent la création de dérivés, leur redistribution ou leur usage commercial au-delà de certains seuils. Le champ `base_model_license` est obligatoire et la couche D refuse toute configuration dont l'exploitation annoncée contredit la licence du modèle de base.

**Cadre juridique applicable depuis la Côte d'Ivoire :** l'activité relève du droit ivoirien et de l'espace OHADA, notamment :

- **Loi n° 2013-450 du 19 juin 2013** relative à la protection des données à caractère personnel : tout traitement de données à caractère personnel est soumis à une déclaration préalable auprès de l'autorité de protection, l'ARTCI ; elle s'applique aux jeux de données d'entraînement et d'évaluation ainsi qu'aux métriques remontées par `report()`.
- **Loi n° 2013-451 du 19 juin 2013** relative à la lutte contre la cybercriminalité, modifiée par la loi n° 2023-593 du 7 juin 2023 : elle encadre l'accès aux systèmes et la sécurité des artefacts diffusés.
- **Loi n° 2013-546 du 30 juillet 2013** relative aux transactions électroniques : elle régit les transactions, la contractualisation et la conservation des documents électroniques de la place de marché (couche F).
- **Droit OHADA** : forme sociale, contrats commerciaux et sûretés des opérateurs et partenaires.

Restent à traiter, par avis d'un conseil inscrit au barreau ivoirien avant commercialisation : propriété des configurations dérivées, responsabilité de l'opérateur de certification, concurrence, contrôle des exportations de technologies et fiscalité transfrontalière des licences.

## 11. Plan de mise en œuvre et feuille de route

### 11.1 Principe

Le projet est porté par le mainteneur, en open source ; les agents IA en sont la force de travail. Les douze premières semaines visent trois preuves successives : un dépôt public opérationnel, une preuve technique mesurée, une première transaction réelle.

### 11.2 Chantier 1 — Le dépôt open source (semaine 1)

Ouverture d'un dépôt public `pucia` sur GitHub, au nom du mainteneur, organisé comme suit :

```text
pucia/
├── spec/            spécification PUCIA et schéma JSON du manifeste
├── pucia/           bibliothèque Python de référence : publier, valider,
│                    certifier, activer, migrer, révoquer
├── registry/        signature des paquets, horodatage des empreintes,
│                    attribution des identifiants OID
├── bench/           bancs de test reproductibles
├── configs/         configurations d'exemple
├── CONTRIBUTING.md  règles de contribution pour les humains et les IA
├── LICENSE          Apache 2.0 pour le code
└── LICENSE-SPEC     CC BY 4.0 pour la spécification
```

**Livrables :** schéma JSON du manifeste validable automatiquement ; outils de signature et d'horodatage ; arc OID PUCIA ouvert sous un PEN IANA du mainteneur ; règles de contribution publiées.

### 11.3 Chantier 2 — La preuve technique, expérience E1 (semaines 2 à 6)

- **Modèle de base :** un petit modèle ouvert, de 1 à 3 milliards de paramètres, sous licence Apache 2.0.
- **Calcul :** processeurs graphiques loués à l'heure, sans achat de matériel.
- **Trois configurations sur des tâches universelles :**
  1. extraction de données dans des documents d'entreprise : factures, contrats, formulaires ;
  2. assistance technique ;
  3. traduction ciblée.
- **Mesure :** coût complet de l'entraînement de chaque configuration, puis coût complet de sa réutilisation par une autre instance, ventilés selon les postes de l'annexe B.
- **Critère de succès :** une réutilisation au moins 30 % moins coûteuse que l'entraînement, à qualité égale ; l'hypothèse H1 est alors démontrée.

### 11.4 Chantier 3 — La preuve par l'argent (semaines 6 à 12)

- **Service PUCIA Registry :** le registre fonctionne sur l'infrastructure de Pixel AI SARLU et délivre le premier certificat PUCIA.
- **Client pilote :** une entreprise qui traite un grand volume de documents (assurance, banque, logistique, administration) acquiert sous licence la configuration certifiée d'extraction documentaire. C'est la première transaction réelle et la première mesure de l'hypothèse H5.
- **Publication :** résultats positifs et négatifs publiés dans le dépôt, puis appel public aux contributeurs humains et IA.

### 11.5 Répartition des rôles

| Acteur | Responsabilités |
|---|---|
| **Mainteneur (Honoré DEMBELE)** | Décisions et intégration au standard ; ouverture des comptes et du dépôt ; agrément des validateurs ; désignation du suppléant ; prospection et contractualisation du client pilote via Pixel AI SARLU ; fixation des plafonds de dépenses. |
| **Agents IA (Claude, ChatGPT et autres)** | Rédaction du code, du schéma et des tests ; exécution des expériences dans l'enceinte ; documentation et rapports ; critique et contributions transmises au mainteneur sous forme de propositions publiques. |

### 11.6 Feuille de route longue

| Période | Travaux | Livrable / décision |
|---|---|---|
| J1–J15 | Modèle, benchmarks, manifeste, équipe ; publication du règlement de certification ; désignation écrite du suppléant ; ouverture du dépôt public sous CC BY 4.0 et Apache 2.0 ; mise en place de l'enceinte et des plafonds | Spécification 0.1 ; hypothèses pré-enregistrées et horodatées ; règles de contribution publiées. |
| J16–J35 | Trois configurations, transfert | Démonstration E1 et mesures. |
| J36–J55 | Coûts, qualité, sécurité | Rapport économique pilote. |
| J56–J75 | Multi-agents, E2/E4 | Comparatif scientifique reproductible. |
| J76–J90 | Standard et catalogue prototypes | PUCIA 0.2 ; décision poursuivre/arrêter. |
| M4–M6 | 2–3 partenaires pilotes | Transactions réelles ou arrêt. |
| M7–M12 | Interopérabilité, bibliothèque, E3 | PUCIA 1.0 si critères atteints. |
| Année 2 | Prédiction et audits externes | Résultats sur tâches inédites. |
| Année 3 | Architecture fixe à plus grande échelle | Généralisation ou réorientation. |

## 12. Ressources et budgets

**Équipe indicative :** responsable scientifique IA (1), ingénieurs ML (2), MLOps/sécurité (1), développeur protocole/catalogue (1), économiste/partenariats à temps partiel, juriste en mission.

**Budgets indicatifs sur 90 jours — scénarios de planification, pas devis :**

| Poste | Frugal (USD) | Renforcé (USD) |
|---|---:|---:|
| Calcul et hébergement | 2 000 | 15 000 |
| Ingénierie et recherche | 12 000 | 60 000 |
| Sécurité, juridique, évaluation | 2 000 | 12 000 |
| Infrastructure, données, outils | 1 500 | 8 000 |
| Imprévus | 2 500 | 10 000 |
| **Total** | **20 000** | **105 000** |

Ces budgets ne couvrent ni l'entraînement d'un modèle de fondation depuis zéro, ni une infrastructure mondiale. Les montants seront arrêtés sur devis.

**Financement progressif :** preuve de concept → deux pilotes payants ou subvention → marché uniquement après validation de la demande → fondation de standardisation indépendante si justifiée.

## 13. Conditions d'échec et décisions

**La thèse pourrait échouer si :** la validation coûte plus cher qu'une adaptation locale ; les configurations sont trop peu transférables ; le stockage externe augmente sans limite ; les configurations accumulées ne permettent pas de prédire de nouvelles tâches ; les entreprises refusent de partager malgré les économies ; les spécialisations dégradent trop la polyvalence ou la sécurité ; les changements de version des modèles de base rendent le catalogue obsolète plus vite qu'il ne s'amortit.

**Jalons de décision :**

- **J35 :** transfert fiable ?
- **J55 :** gain économique reproductible ?
- **J90 :** prototype stable et protocole auditable ?
- **M12 :** partenaires et réutilisations réelles ?

Si un critère échoue, documenter le résultat, réviser l'hypothèse ou arrêter le volet concerné.

## 14. Livrables

1. Spécification PUCIA et schéma du manifeste.
2. Dépôt de code reproductible, tests et configurations d'exemple.
3. Catalogue expérimental signé, horodaté et versionné, avec identifiants OID.
4. Rapport comparatif coûts / qualité / temps / énergie / stockage.
5. Livre blanc avec résultats positifs **et négatifs**.
6. Dossier de partenariat pour laboratoires, universités et industriels.

**Conclusion :** la première victoire n'est pas la programmation instantanée universelle ; c'est la preuve qu'une configuration validée, certifiée et mutualisée procure une économie immédiate mesurable. Ensuite seulement, l'accumulation de configurations permettra de tester la prédiction de configurations inédites à budget maîtrisé.

## Annexe A — Chaîne conceptuelle

```text
MODÈLE DE RÉFÉRENCE
  → CONFIGURATIONS SPÉCIALISÉES
  → SIGNATURE ET HORODATAGE
  → VALIDATION INDÉPENDANTE ET CERTIFICATION
  → REGISTRE COMMUN (IDENTIFIANTS OID)
  → RÉUTILISATION / LICENCES
  → DONNÉES DE PERFORMANCE
  → APPRENTISSAGE DES RÉGULARITÉS
  → PRÉDICTION DE NOUVELLES CONFIGURATIONS
  → VALIDATION INDÉPENDANTE (boucle)
```

## Annexe B — Variables minimales de recherche

| Variable | Contenu |
|---|---|
| `task_id` | Identifiant et version de tâche. |
| `pucia_oid` | Identifiant de la configuration dans le registre. |
| `base_hash` | Empreinte du modèle de référence. |
| `config_hash` | Empreinte de configuration. |
| `parameter_budget` | Poids totaux, actifs, externes. |
| `storage_per_task_bytes` | Stockage propre à la compétence (masque, vecteur, adaptateur). |
| `switch_latency_ms` | Latence de bascule. |
| `training_cost_usd` | Coût complet de production, ventilé : données, annotation, calcul, évaluation, ingénierie. |
| `reuse_cost_usd` | Coût complet de réutilisation. |
| `quality_score` | Benchmark indépendant. |
| `regression_score` | Perte sur compétences précédentes. |
| `license_id` | Licence et droits de redistribution. |
| `base_model_license` | Licence du modèle de base. |

## Annexe C — Glossaire

- **Configuration :** instructions ou artefacts modifiant l'utilisation d'un modèle.
- **Paramètres :** valeurs numériques apprises et stockées par un réseau neuronal.
- **LoRA :** adaptation à faible rang, ajoutant généralement des poids entraînables.
- **Masque binaire :** sélection, par tâche, des poids actifs d'un réseau figé ; coûte 1 bit par paramètre et par tâche.
- **Vecteur de tâche :** différence entre les poids d'un modèle spécialisé et ceux du modèle de base, combinable par addition ou négation.
- **Hyperréseau :** réseau produisant tout ou partie des poids d'un autre réseau.
- **Méta-apprentissage :** apprentissage visant une adaptation plus efficace à de nouvelles tâches.
- **Mutualisation :** partage contrôlé de résultats et configurations.
- **Budget fixe :** plafond explicitement défini sur les ressources et paramètres comptabilisés.
- **OID :** identifiant d'objet hiérarchique et pérenne ; un numéro d'entreprise privée (PEN) attribué par l'IANA ouvre un arc sous lequel le titulaire attribue ses propres identifiants.
- **Horodatage :** preuve cryptographique qu'une empreinte existait à une date donnée, établissant l'antériorité d'une publication.

## Annexe D — Références de départ

- Hu et al., *LoRA: Low-Rank Adaptation of Large Language Models*, arXiv:2106.09685.
- Ha, Dai et Le, *HyperNetworks*, arXiv:1609.09106.
- Fedus, Zoph et Shazeer, *Switch Transformers*, arXiv:2101.03961.
- McMahan et al., *Communication-Efficient Learning of Deep Networks from Decentralized Data*, arXiv:1602.05629.
- Mallya, Davis et Lazebnik, *Piggyback: Adapting a Single Network to Multiple Tasks by Learning to Mask Weights*, ECCV 2018, arXiv:1801.06519.
- Ilharco et al., *Editing Models with Task Arithmetic*, ICLR 2023, arXiv:2212.04089.
- Huang et al., *LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition*, arXiv:2307.13269.
- Charakorn, Cetin, Tang et Lange, *Text-to-LoRA: Instant Transformer Adaption*, ICML 2025, arXiv:2506.06105.
- Hugging Face PEFT : https://huggingface.co/docs/peft/index
- MLCommons MLPerf : https://mlcommons.org/benchmarks/
- NVIDIA NIM : https://docs.nvidia.com/nim/
- République de Côte d'Ivoire : loi n° 2013-450 du 19 juin 2013 (données à caractère personnel) ; loi n° 2013-451 du 19 juin 2013 (cybercriminalité), modifiée par la loi n° 2023-593 du 7 juin 2023 ; loi n° 2013-546 du 30 juillet 2013 (transactions électroniques).

Ces références sont des pistes techniques et juridiques, **pas des validations de PUCIA**.

---

## Mission proposée à toute IA recevant ce document

**Évaluer PUCIA de façon critique et constructive.** Identifier les hypothèses les plus fragiles, proposer des expériences falsifiables, estimer les ressources nécessaires et suggérer des architectures respectant un budget total de paramètres explicite. Comparer systématiquement avec les techniques existantes recensées en section 3 ; ne pas présenter comme découvert ce qui n'a pas été démontré. Produire des contributions documentées, testables et partageables, sans entreprendre d'actions externes non autorisées.

**Forme des contributions.** Toute contribution est rédigée comme une proposition publique comprenant : la section du document visée, la modification proposée, la justification, le test permettant de la vérifier et, le cas échéant, les références. Les contributions sont examinées selon les règles de la section 7 et intégrées au standard par décision du mainteneur, Honoré DEMBELE. Elles sont versées sous les licences du projet (section 10.2).
