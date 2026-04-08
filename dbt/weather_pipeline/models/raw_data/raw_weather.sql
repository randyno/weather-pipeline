{{ config(materialized = 'table') }}

SELECT *
FROM read_csv_auto('/app/data/dbt_raw/open-meteo*.csv')