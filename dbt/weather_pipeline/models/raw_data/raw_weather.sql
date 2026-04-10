{{ config(materialized = 'table') }}

SELECT 
    datetime_hour,
    insertion_time, 
    temperature_2m, 
    relative_humidity_2m, 
    apparent_temperature, 
    rain, 
    cloud_cover, 
    wind_speed_10m, 
    precipitation
FROM read_csv_auto('/app/data/dbt_raw/open-meteo-2026-04-10 15-33.csv', header=True)