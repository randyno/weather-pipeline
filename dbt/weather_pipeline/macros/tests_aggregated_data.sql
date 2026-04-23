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
