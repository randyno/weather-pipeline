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
FROM read_csv_auto('/app/data/dbt_raw/open-meteo-weather-data.csv', header=True)