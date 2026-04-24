{% macro test_is_positive(model, column_name) %}

    SELECT {{ column_name}}
    FROM {{ model}}
    WHERE {{ column_name}} < 0

{% endmacro %}

{% macro test_is_between(model, column_name, min_value, max_value) %}

    SELECT {{ column_name}}
    FROM {{ model}}
    WHERE {{ column_name}} NOT BETWEEN {{ min_value }} AND {{ max_value }}

{% endmacro %}

{% macro test_no_missing_date(model, column_name) %}

    WITH today_yesterday AS(
        SELECT {{ column_name }} as day_N,
            -- Get the date last date before day_N, replace by 2026-03-01 for day_0
            LAG({{ column_name }}, 1, 
                CAST('2026-03-01' AS DATE))
                OVER (ORDER BY  {{ column_name }} ) AS day_N_minus_1
        FROM {{ model }}
    )
    SELECT *
    FROM today_yesterday
    WHERE day_N - day_N_minus_1 > 1

{% endmacro %}

-- {% macro test_uptodate(model, column_name) %}

--     WITH today AS (
--         SELECT CAST(now() AS DATE) AS today_
--         FROM {{ model }}
--     )
--     SELECT * 
--     FROM {{ model}}
--     WHERE max({{ column_name}}) 

-- {% endmacro %}