# Structure du System Architecture Design (SAD)

## 1. Vue d'ensemble (High-Level Overview)
Explique l'objectif du système : fournir une plateforme de visualisation météorologique automatisée.
* **Objectif :** Collecter, transformer et visualiser les données météorologiques(température, précipitations, vitesse du vent, humidité) de mars à aujourd'hui.
* **Flux global :** API Open-Meteo → Ingestion Python → Stockage Fichier CSV → Transformation dbt → Stockage duckDB → Dashboard Streamlit.

## 2. Diagramme d'Architecture

* **Service `weather-db` :** Script Python d'extraction (EL): On charge les données en requêtant l'API Open-meteo et on les garde dans un fichier `.csv`.
* **Service `weather_dbt` :** Couche de transformation SQL (T): Le fichier `.csv` sert de source pour les modèles dbt. 
raw_weather(read_csv) 
--> cleaned_weather(données nettoyées et transformées au bon type et bon format)
--> aggregated_data(Données aggrégées) :
        - daily_aggregates
        - hourly_aggregates
* **Service `dashboards` :** Interface utilisateur codée avec Streamlit

Chaque micro service a sa propre image python avec des dependances differentes.

## 3. Choix Technologiques et Justifications

### Serveur de données :
Nous avions deux possibilités :
- MySQL (déjà utilisé avant)
- DuckDB (suite à une recommandation pour ce cas d'usage)

| Caractéristiques | MySQL | DuckDB |
| Type | Serveur (Lourd) | Fichier (Léger)|
| Installation | Nouveau service Docker | Juste une library Python |
| Vitesse (Calculs) | Standard | Très rapide (Vectorisé) |
| Lecture CSV | Import manuel requis | Lecture directe native |
| Usage idéal | Application Web | Pipeline de données / dbt |

==> `DuckDB` car simple a installer, rapide, lit les fichiers `.csv` 


### dbt (Data Build Tool) :
Utilisé pour modulariser les transformations SQL (agrégats horaires vs journaliers) et garantir la qualité des données.

### Docker Compose :
Sélectionné pour garantir la portabilité du projet, permettant de lancer l'infrastructure complète avec une seule commande, malgré les défis de droits d'accès sur les volumes montés.

### Outil de visualisation 
* Le choix s'est porté sur `Streamlit` afin de maximiser le temps passé sur la logique des données au detriment de l'infrastructure 'Front End'. L'objectif était de livrer un produit fonctionnel rapidement sans la complexité liée à l'emploi des Framework web (React, Flask)
* `Streamlit` bénéficie d'une adoption massive dans la communauté Data. Cela garantit une maintenance robuste, une documentation riche et une facilité de déploiement (Cloud-ready), ce qui sécurise la maintenance à long terme du projet.

## 4. Gestion de la Donnée (Data Management)

* **Persistance :** Utilisation d'un volume Docker monté sur `./data` pour conserver le fichier `.duckdb` entre les redémarrages de services.

* **Problème de lecture seule (Read-Only) :** Puisque DuckDB est une base de donnees fichier, les transactions ne sont pas gerees par un server. Afin d'eviter les conflits d'acces entre les differents services, nous avons attribue a `Dashboards` (streamlit) une connection en lecture seule et a dbt le droit d'ecriture. 
 
* **Granularité :** Le système gère deux niveaux de précision : l'heure pour les tendances intra-journalières (servant a analyser les tendances intra-journalieres) et le jour pour les records historiques(jour le plus chaud).

## 5. Sécurité et Portabilité
 
* **Dépendances :** 
- Utilisation d'images Docker légères (type Python-slim) pour optimiser la taille du projet.
- Chaque micro-service utilise sa propre image et possède ses propres dependances python.
- Pour le passage en production (Cloud), le projet prévoit l'utilisation d'utilisateurs non-root dans les containers afin d'éviter les attaques sur la chaîne d'approvisionnement

## 6. Evolution & Scalabilite
Bien que pour le moment le projet a un usage local, l'objectif est de pouvoir le deployer sur n'importe quel Serveur d'où l'utilisation de Docker et dbt qui vont permettre une migraiton facile vers un orchestrateur comme Airflow ou un deploiement Cloud (GCP/AWS) sans modification majeure du code.