

{{ config(materialized='table') }}

WITH source_data AS (
    SELECT DISTINCT
        CAST(datetime_hour AS STRING) AS pKey,
        CAST(insertion_time AS TIMESTAMP) AS _insertion_time,
        strftime(datetime_hour, '%Y-%m-%d') as day,
        CAST (datetime_hour AS TIMESTAMP) AS date_hour,
        CAST(temperature_2m AS FLOAT) AS temperature_2m,
        CAST(relative_humidity_2m AS INT64) AS humidity,
        CAST(apparent_temperature AS FLOAT) AS apparent_temperature,
        CAST(rain AS FLOAT) AS rain,
        CAST(cloud_cover AS INT64) AS cloud_cover,
        CAST(wind_speed_10m AS FLOAT) AS wind_speed,
        precipitation 
    FROM {{ ref('raw_weather') }}
    ORDER BY day, date_hour
),
ordered_data AS(
    SELECT 
        source_data.*,
        ROW_NUMBER() OVER(
            PARTITION BY day, date_hour
            ORDER BY _insertion_time DESC
        ) AS most_recent
    from source_data
)

SELECT
    ordered_data.*EXCLUDE(most_recent) --Use EXCEPT if we switch to BigQuery
FROM ordered_data
WHERE most_recent = 1
