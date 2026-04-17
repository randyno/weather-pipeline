
# 1. Le Data Dictionary (ou Data Catalogue)



**Ce que tu dois inclure :**
* **Les Sources (Raw Data) :** Donnees brutes recoltees d'open-meteo API
    - `datetime_hour`  (TIMESTAMP)    : date et heure de la mesure 
    - `insertion_time` (TIMESTAMP)    : heure et date a laquelle la donnee a ete telechargee de Open-meteo
    - `temperature_2m` (DOUBLE)       : Mesure de la temperature en °C 2 metres au dessus du sol
    - `relative_humidity_2m` (BIGINT) : Mesure du taux d'humidite relative (en %) 2 metres au dessus du sol
    - `apparent_temperature` (DOUBLE) : Temperature apparente en °C
    - `rain` (DOUBLE)                 : Mesure de la pluie en mm
    - `cloud_cover` (BIGINT)          : Mesure du taux de couverture des nuages en %
    - `wind_speed_10m` (DOUBLE)       : Mesure de la vitesse des vents en km/h 10 metres au dessus du sol
    - `precipitation` (DOUBLE)        : Mesure des precipitations (pluies, neige, grêle) en mm

* **Table d'aggregats 1 : `daily_aggregates`** 
    - `day` date : date de la journee (Format %Y-%m-%D)
    - `avg_temperature_2m` DOUBLE : Moyenne des temperatures 2 metres au dessus du sol dans la journee
    - `avg_humidity` DOUBLE : Humidite moyenne sur la journee
    - `avg_apparent_temperature` DOUBLE : Moyenne des temperatures ressenties dans la journee
    - `total_rain` DOUBLE : Total des pluies dans la journee
    - `avg_cloud_cover` DOUBLE : Couverture moyenne des nuages dans la journee
    - `avg_wind_speed` DOUBLE : vitesse moyenne du vents dans la journee
    - `total_precipitation` DOUBLE : Total des precipitations(pluies, neige, grêle) de la journee en mm
    - `max_temperature_2m` FLOAT : pic de chaleur releve sur la journee
    - `min_temperature_2m` FLOAT : creux de chaleur releve sur la journee
    - `temperature_range` FLOAT : difference de temperature la temperature la plus haute et la plus basse de la journee
    - `apparent_temperature_range` FLOAT : difference de temperature apparente entre l'heure la plus chaude et l'heure la moins chaude en de la journee

* **Table d'aggregats 2 : `hourly_aggregates`** 
Les differents indicateurs sont aggreges en se basant sur l'heure `hours` comme des profils journaliers.
    - `hours` string : heure de la journee (Format HH:MM:SS)
    - `avg_temperature_2m` DOUBLE : moyenne des temperatures sur l'heure HH 
    - `max_temperature_2m` FLOAT : Température maximale relevée à 2 mètres du sol sur l'heure.
    - `min_temperature_2m` FLOAT : Température minimale relevée à 2 mètres du sol sur l'heure.
    - `avg_humidity` DOUBLE : Humidité relative moyenne (%) calculée sur l'intervalle horaire.
    - `max_humidity` BIGINT : Valeur maximale de l'humidité relative (%) sur l'heure.
    - `min_humidity` BIGINT : Valeur minimale de l'humidité relative (%) sur l'heure.
    - `avg_apparent_temperature` DOUBLE : Moyenne de la température ressentie (index de confort thermique).
    - `max_apparent_temperature` FLOAT : Température ressentie maximale relevée sur l'heure.
    - `min_apparent_temperature` FLOAT : Température ressentie minimale relevée sur l'heure.
    - `avg_rain` DOUBLE : Intensité moyenne de la pluie (mm) sur l'heure.
    - `max_rain` FLOAT : Intensité maximale de la pluie relevée sur l'heure.
    - `min_rain` FLOAT : Intensité minimale de la pluie relevée sur l'heure.
    - `avg_cloud_cover` DOUBLE : Couverture nuageuse moyenne (%) sur l'heure.
    - `max_cloud_cover` BIGINT : Pourcentage maximal de couverture nuageuse sur l'heure.
    - `min_cloud_cover` BIGINT : Pourcentage minimal de couverture nuageuse sur l'heure.
    - `avg_wind_speed` DOUBLE : Vitesse moyenne du vent (km/h) sur l'intervalle horaire.
    - `max_wind_speed` FLOAT : Vitesse maximale du vent relevée sur l'heure.
    - `min_wind_speed` FLOAT : Vitesse minimale du vent relevée sur l'heure.
    - `avg_precipitation` DOUBLE : Cumul moyen des précipitations (pluie + neige + grêle) en mm.
    - `max_precipitation` DOUBLE : Valeur maximale des précipitations relevées sur l'heure.
    - `min_precipitation` DOUBLE : Valeur minimale des précipitations relevées sur l'heure.

### Une petite question pour ton dbt :
As-tu déjà généré la documentation native de dbt via la commande `dbt docs generate` ? C'est une fonctionnalité incroyable qui crée un site web interactif montrant ton "Lineage Graph" (le schéma de dépendance de tes tables). Si tu l'as fait, tu peux simplement mettre une capture d'écran de ce graphe dans ton Data Dictionary !

**Souhaites-tu que nous rédigions ensemble la description d'une de tes tables dbt pour ton dictionnaire ?**