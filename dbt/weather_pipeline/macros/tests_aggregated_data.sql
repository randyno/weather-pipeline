{% test is_positive(model, column_name) %}

    SELECT {{ column_name}}
    FROM {{ model}}
    WHERE {{ column_name}} < 0

{% endtest %}

{% test is_between(model, column_name, min_value, max_value) %}

    SELECT {{ column_name}}
    FROM {{ model}}
    WHERE {{ column_name}} BETWEEN (min_value, max_value)

{% endtest %}

{% test no_missing_date(model, date_column)}

    WITH today_yesterday AS(
        SELECT {{ date_column }} as day_N,
            -- Get the date last date before day_N, replace by 2026-03-01 for day_0
            LAG({{ date_column }}, 1, strftime('2026-03-01','%Y-%m-%D'))
                OVER (ORDER BY  {{ date_column }} ) AS day_N_minus_1
        FROM {{ model }}
    )
    SELECT *
    FROM today_yesterday
    WHERE day_N - day_N_minus_1 > 1

{% endtest %}