# Tests a realiser 

## 1. Weather-db
- Vérifier que le fichier weather_*.csv est bien généré [v]
- The "API Response" Check: Tester la reaction du script a la reponse 500 (internal error) de l'API
- Vérifier que toutes les colonnes sont bien présentes et bien nommées
- Vérifier qu'il contient les données de toutes les journées entre le 1er mars et la date du jour [x]

## 2. Weather_dbt

### Data checks

1. The "Dry Day" Check: Ensure that `total_rain` and `total_precipitation` are never negative values.

2. The "Unique Hour" Check: Ensure that in `hourly_aggregates`, there is only one entry per hours string (no duplicates).

3. The "Extreme Heat" Check: Alerte si `max_temperature_2m` excede une valeur physiquement impossible (60 degres).

4. The "Relationship" Check: Assure que chaque date existe bien dans la table source.

5. The "Humidity Percent" Check: Assure que `relative_humidity_2m` est toujours entre 0 et 100.

6. The "Empty Table" Check: Alerte si la table `daily_aggregates` est completement vide apres l'execution de dbt run

7. Data Continuity : Pas de trou dans les donnees. 

### Logic Tests
1. The "Range Math" Check: Verify that temperature_range is exactly equal to max_temperature_2m - min_temperature_2m.

 
## 3. Dashboards
- Vérifier que la page web affiche bien les données 
