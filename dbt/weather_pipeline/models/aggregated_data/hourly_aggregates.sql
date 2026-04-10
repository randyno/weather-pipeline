{{ config(materialized='table') }}

WITH hourly_data AS (
    SELECT 
        STRING_TO_ARRAY(pkey, ' ')[2] AS hours, --pKey format is "2026-04-10 15:00:00" 
        * EXCLUDE(pKey, _insertion_time, date_hour) --Use EXCEPT if we switch to BigQuery
    FROM {{ ref("cleaned_weather") }}
)

SELECT
    hours,
    ROUND(AVG(temperature_2m), 2) AS avg_temperature_2m,
    MAX(temperature_2m) AS max_temperature_2m,
    MIN(temperature_2m) AS min_temperature_2m,
    ROUND(AVG(humidity), 2) AS avg_humidity,
    MAX(humidity) AS max_humidity,
    MIN(humidity) AS min_humidity,
    ROUND(AVG(apparent_temperature), 2) AS avg_apparent_temperature,
    MAX(apparent_temperature) AS max_apparent_temperature,
    MIN(apparent_temperature) AS min_apparent_temperature,
    ROUND(AVG(rain), 2) AS avg_rain,
    MAX(rain) AS max_rain,
    MIN(rain) AS min_rain,
    ROUND(AVG(cloud_cover), 2) AS avg_cloud_cover,
    MAX(cloud_cover) AS max_cloud_cover,
    MIN(cloud_cover) AS min_cloud_cover,
    ROUND(AVG(wind_speed), 2) AS avg_wind_speed,
    MAX(wind_speed) AS max_wind_speed,
    MIN(wind_speed) AS min_wind_speed,
    ROUND(AVG(precipitation), 2) AS avg_precipitation,
    MAX(precipitation) AS max_precipitation,
    MIN(precipitation) AS min_precipitation
FROM hourly_data
GROUP BY hours
ORDER BY hours