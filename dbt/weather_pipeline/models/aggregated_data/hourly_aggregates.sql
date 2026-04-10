{{ config(materialized='table') }}

WITH hourly_data AS (
    SELECT 
        STRING_TO_ARRAY(pkey, ' ')[2] AS hours, --pKey format is "2026-04-10 15:00:00" 
        * EXCLUDE(pKey, _insertion_time, date_hour) --Use EXCEPT if we switch to BigQuery
    FROM {{ ref("cleaned_weather") }}
)

SELECT
    hours,
    AVG(temperature_2m) AS avg_temperature_2m,
    MAX(temperature_2m) AS max_temperature_2m,
    MIN(temperature_2m) AS min_temperature_2m,
    AVG(humidity) AS avg_humidity,
    MAX(humidity) AS max_humidity,
    MIN(humidity) AS min_humidity,
    AVG(apparent_temperature) AS avg_apparent_temperature,
    MAX(apparent_temperature) AS max_apparent_temperature,
    MIN(apparent_temperature) AS min_apparent_temperature,
    AVG(rain) AS avg_rain,
    MAX(rain) AS max_rain,
    MIN(rain) AS min_rain,
    AVG(cloud_cover) AS avg_cloud_cover,
    MAX(cloud_cover) AS max_cloud_cover,
    MIN(cloud_cover) AS min_cloud_cover,
    AVG(wind_speed) AS avg_wind_speed,
    MAX(wind_speed) AS max_wind_speed,
    MIN(wind_speed) AS min_wind_speed,
    AVG(precipitation) AS avg_precipitation,
    MAX(precipitation) AS max_precipitation,
    MIN(precipitation) AS min_precipitation
FROM hourly_data
GROUP BY hours
ORDER BY hours