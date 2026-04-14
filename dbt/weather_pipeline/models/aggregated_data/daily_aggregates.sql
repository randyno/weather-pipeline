{{ config(materialized = 'table') }}

SELECT
    CAST(day AS DATE) AS day,
    ROUND(AVG(temperature_2m), 2) AS avg_temperature_2m,
    ROUND(AVG(humidity), 2) AS avg_humidity,
    ROUND(AVG(apparent_temperature), 2) AS avg_apparent_temperature,
    ROUND(SUM(rain), 2) AS total_rain,
    ROUND(AVG(cloud_cover), 2) AS avg_cloud_cover,
    ROUND(AVG(wind_speed), 2) AS avg_wind_speed,
    ROUND(SUM(precipitation), 2) AS total_precipitation,
    ROUND(MAX(temperature_2m),2) AS max_temperature_2m,
    ROUND(MIN(temperature_2m),2) AS min_temperature_2m,
    ROUND(MAX(temperature_2m) - MIN(temperature_2m),2) AS temperature_range,
    ROUND(MAX(apparent_temperature) - MIN(apparent_temperature),2) AS apparent_temperature_range
FROM {{ ref('cleaned_weather') }}
GROUP BY day
ORDER BY day