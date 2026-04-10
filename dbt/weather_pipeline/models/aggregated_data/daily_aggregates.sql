{{ config(materialized = 'table') }}

SELECT
    day,
    AVG(temperature_2m) AS avg_temperature_2m,
    AVG(humidity) AS avg_humidity,
    AVG(apparent_temperature) AS avg_apparent_temperature,
    SUM(rain) AS total_rain,
    AVG(cloud_cover) AS avg_cloud_cover,
    AVG(wind_speed) AS avg_wind_speed,
    SUM(precipitation) AS total_precipitation,
    MAX(temperature_2m) AS max_temperature_2m,
    MIN(temperature_2m) AS min_temperature_2m,
    MAX(temperature_2m) - MIN(temperature_2m) AS temperature_range,
    MAX(apparent_temperature) - MIN(apparent_temperature) AS apparent_temperature_range,
FROM {{ ref('cleaned_weather') }}
GROUP BY day
ORDER BY day