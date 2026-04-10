# Idees d'analyses a mettre en place

## 1. Analyses Temporelles (Le classique indispensable)
C'est la base pour comprendre les cycles.
* **Profil Journalier Moyen :** Calcule la température moyenne par heure sur tout ton historique. *Application :* À quelle heure fait-il réellement le plus chaud chez toi ? Est-ce 14h ou 16h ?
* **Amplitude Thermique :** Calcule la différence entre le `MAX(temp)` et le `MIN(temp)` par jour. *Application :* Identifier les jours de "choc thermique" où le temps a radicalement changé.
* **Calcul du "Point de Rosée" :** Si tu as l'humidité et la température, tu peux calculer si l'air est saturé. *Application :* Prédire l'apparition du brouillard ou du givre sur ton pare-brise.



---

## 2. Analyses de Corrélation (Le niveau Data Scientist)
Ici, on cherche à voir comment une variable influence l'autre.
* **Nuage de points (Scatter Plot) Vent vs Température :** Est-ce que le vent souffle plus fort quand il fait froid (refroidissement éolien) ?
* **Corrélation Précipitations / Couverture Nuageuse :** À partir de quel pourcentage de nuages la pluie commence-t-elle statistiquement à tomber ?

---

## 3. Applications Pratiques et Domotique
C'est là que ton projet devient utile au quotidien.
* **Indicateur "Étendre le linge" :** Crée un flag (Vrai/Faux) qui combine : pas de pluie prévue dans les 6h + vent > 10km/h + humidité < 60%.
* **Optimisation Énergétique :** Si tu couples tes données météo avec ta consommation de chauffage (si tu as accès à ton compteur), tu peux calculer ton **"Coefficient d'Isolation"** : combien de kWh consommes-tu par degré extérieur en moins ?
* **Alerte Jardinage :** Un modèle dbt qui identifie les "Nuits de Gel" (Temp < 0°C) pour t'envoyer une notification Airflow de protéger tes plantes.



---

## 4. Analyse de la Fiabilité de l'API (Méta-Analyse)
Puisque tu stockes `_insertion_time`, tu as un historique des prévisions.
* **Le test de vérité :** Compare la prévision faite "Il y a 24h" avec ce qui s'est réellement passé (la mesure au temps T).
* **Application :** Est-ce que l'API Open-Meteo est plus fiable pour la pluie ou pour la température ? Est-elle plus précise le matin ou le soir ?

---

## 5. Comment mettre ça en place avec dbt ?
Tu ne vas pas faire ces calculs dans un tableur. Tu vas créer de nouveaux modèles dans ton dossier `models/marts/` :

1.  **`fct_weather_daily.sql`** : Un modèle qui agrège par jour (Moyenne, Max, Min, Somme de pluie).
2.  **`fct_weather_anomalies.sql`** : Un modèle qui compare la température du jour à la moyenne des 7 derniers jours.

### Prochaine étape visuelle ?
Pour rendre ça "sexy", tu pourras connecter un outil de BI (Business Intelligence) léger comme **Evidence.dev** (qui adore DuckDB) ou **Metabase** à ton fichier `.duckdb`. Tu auras alors des graphiques qui se mettent à jour tout seuls à chaque `dbt run`.



**Parmi ces idées, laquelle te semble la plus excitante pour commencer à coder ton prochain modèle SQL ?**