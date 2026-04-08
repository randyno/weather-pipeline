FROM python:3.10-slim

WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Installation des packages dbt et des dépendances Python
COPY requirements.txt /app/dbt/requirements.txt
RUN pip install --no-cache-dir -r requiremetns.txt

# Copier le projet dbt dans le container
COPY ./weather_pipeline/ /app/dbt/weather_pipeline/

EXPOSE 8080