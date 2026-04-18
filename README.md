# weather-pipeline

Un pipeline ELT météo, pensé pour être clonable et fonctionnel en 2 commandes.

## 1. Infos générales sur le projet

### Source de données :
API Open Meteo (gratuite, sans clé)

### Stack :
dbt · DuckDB · Streamlit · Docker

### Architecture :
  
  weather-pipeline/

  ├── docker-compose.yml

  ├── weather-db/
  
  │   ├── main.py

  │   ├── Dockerfile

  │   ├── requirements.txt
  
  ├── dbt/

  │   ├── Dockerfile

  │   ├── requirements.txt
  
  │   ├── weather_pipeline/ # dbt project
  
  ├── data/raw/*.json

  ├── data/raw/weather-
  
  ├── Dashboards/
  
  │   ├── app.py

  │   ├── Dockerfile

  │   ├── requirements.txt

  └── README.md
  

## 2. Le Guide d'Installation & d'Exploitation (Ops Manual)


### Pré-requis :

- `Docker` et `Docker Compose` installés
- Si vous êtes sur MAC ou Windows : installer aussi `Docker Desktop` 
- Si vous êtes sur Linux : installer `Docker Engine`

### Procédure de démarrage à froid (Cold Start) :
Après avoir cloné le projet, assurez-vous que Docker Desktop soit lancé.

Lancer les commandes suivantes successivement :

* `docker compose up weather-db` : Pour l'ingestion initiale. 
Le micro-service telecharge via l'API open-meteo, les donnees meteo commencant le 1er Mars et s'arrete a la date du jour

* `docker compose run weather_dbt` : Pour transformer les données.
DBT transforme les donnees et les stocke dans une BDD duckDB.

* `docker compose up dashboards` : Pour lancer le dashboard.
Streamlit affiche un visuel des donnees aggregees en lisant la base de donnees

### Maintenance : 
Si les donnees ne sont pas a jour, lancer la commande `docker compose up weather-db` et a la fin de l'execution, les donnees seront a jour.

### Depannage de la base de donnees :

#### Problème : Base de données corrompue ou Verrouillée (Locked)
Si DuckDB affiche une erreur de type Database Error: `Could not set write lock` de façon persistante ou si le fichier `data/dbt_raw/<nom_bdd>.duckdb` semble corrompu, suivez ces étapes :

1. Arrêt des services : 
Stopper tous les conteneurs pour libérer les accès au fichier `.duckdb`:
`docker compose down --remove-ophans`

2. Suppression du fichier `.duckdb`: 
DuckDB étant une base de données "monolithique" stockée dans un seul fichier, la méthode la plus propre pour repartir de zéro est de supprimer le fichier physique dans le volume monté :

`rm ./data/weather_data.duckdb` . 
Ou alors le supprimer manuellement

3. Réinitialisation complète : Relancer la chaîne d'ingestion et de transformation pour recréer une base saine :
`docker compose up weather-db` puis `docker compose run weather_dbt dbt run`.

4. Vérification des fichiers .wal : 
S'il existe un fichier .wal (Write-Ahead Log) dans le dossier /data alors que les containers sont éteints, il faut aussi le supprimer ; c'est souvent lui qui contient les transactions interrompues causant des soucis au redémarrage.


#### Ports déjà utilisés : 
Si vous avez un conflit avec les ports (Un programme sur votre PC utilise déjà les ports que les docker souhaite exploiter), alors il faudra les changer dans le fichier `docker-compose.yml` à la racine du projet.

### Autres :

- Comment vérifier les logs d'un conteneur : `docker logs <container_name>`.
