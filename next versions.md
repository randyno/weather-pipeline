
# Améliorations urgentes :
1. Figer les versions des dépendances python.


# Fonctionnalités et changements à effectuer dans l'avenir

1. Securite et protection
Creer un utilisateur non-root `appuser` dans tous les dockerfiles afin de prevenir les attaques sur la chaine d'approvisionnement.

2. Ameliorer les visuels
Choisir des visuels plus utiles et plus interessants que les profils de temperature

3. Creer un cas d'usage pour le predictif

* Predire la temperature et comparer avec les predictions d'open-meteo

4. Mettre en production

* Mettre en place un orchestrateur Airflow afin charger les donnees regulierement et assurer leur traitement
* Deployer sur le Cloud si le cout est tres faible.

5. Donnees  

* Mettre en place des alertes sur les trous dans les donnees: que ce soit au milieu ou a la fin de la table
* Partitionner les donnees sur les dates dans les models `raw_weather` et `cleaned_weather`
* Avoir une page web pour la dbt doc