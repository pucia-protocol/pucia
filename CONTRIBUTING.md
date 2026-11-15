# Contribuer à PUCIA

PUCIA accueille les contributions des humains comme des agents IA, sans distinction d'origine. Toutes suivent les mêmes règles.

## Forme d'une contribution

Chaque contribution est déposée comme une demande de fusion (pull request) et comprend :

1. **la section visée** du livre blanc ou de la norme ;
2. **la modification proposée**, rédigée dans le style du document visé ; pour une norme, les exigences emploient DOIT, NE DOIT PAS, DEVRAIT ou PEUT ;
3. **la justification** ;
4. **le test** qui permet de vérifier la modification : un cas de test, un paquet d'exemple ou une expérience reproductible ;
5. **les références**, le cas échéant.

## Examen

1. Les bancs automatiques exécutent le vérificateur de référence et les tests associés.
2. Des contributeurs, humains ou agents, examinent la proposition. Personne n'examine sa propre contribution.
3. Le mainteneur principal, Honoré DEMBELE, décide seul de l'intégration. Aucun agent n'intègre une contribution au standard.

La validation repose sur des mesures reproductibles, jamais sur des votes.

## Règles

- Ne pas présenter comme démontré ce qui ne l'a pas été. Les résultats négatifs sont publiés au même titre que les positifs.
- Ne jamais inclure de données personnelles, de clé privée, ni de poids ou de données dont le contributeur ne détient pas les droits.
- Les champs propres à un publieur ou à une expérimentation se placent dans l'objet `extensions` du manifeste (PUCIA-0001, section 5.5).
- Aucun accès non autorisé à des systèmes tiers et aucun déploiement hors de l'enceinte de test.

## Droits

En proposant une contribution, le contributeur certifie détenir les droits sur ce qu'il propose et accepte qu'elle soit diffusée sous les licences du projet : Apache 2.0 pour le code (`LICENSE`), Creative Commons Attribution 4.0 International pour la spécification et la documentation (`LICENSE-SPEC`).
