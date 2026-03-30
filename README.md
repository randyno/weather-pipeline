# weather-pipeline

Un pipeline ELT météo en temps réel, pensé pour être clonable et fonctionnel en 2 commandes.

## Source de données :
API Open Meteo (gratuite, sans clé)
## Stack :
Astro CLI (Airflow léger) · dbt · DuckDB · Streamlit · Docker

## Architecture :
  1. DAG Airflow  →  fetch l'API et stocke un CSV brut dans data/raw/
  2. dbt staging  →  nettoyage + typage des données brutes
  3. dbt mart     →  agrégats prêts à consommer (moyennes, tendances)
  4. Dashboard    →  Streamlit qui lit les marts et affiche les courbes

## Structure du repo :
  weather-pipeline/
  
  ├── dags/         → weather_dag.py
  
  ├── dbt/
  
  │   ├── models/
  
  │   │   ├── staging/
  
  │   │   └── mart/
  
  │   └── tests/
  
  ├── data/raw/
  
  ├── dashboard/    → app.py
  
  ├── Dockerfile
  
  └── README.md
  
── CE QU'IL RESTE À DÉCIDER ───────────────

  • Quelle(s) ville(s) ? → Paris + une autre suggérée
  • Quelles métriques ?  → température, précipitations, vent, humidité
  • Quelle fréquence ?   → toutes les heures ou une fois par jour


── PLAN DE TRAVAIL (2-3h) ──────────────────

  45 min  → DAG Airflow : fetch API + stockage CSV
  60 min  → Modèles dbt : 1 staging + 1 mart + 2 tests qualité
  30 min  → Dashboard Streamlit
  30 min  → README + docker compose up + push GitHub
