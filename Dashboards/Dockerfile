FROM python:3.9-slim

WORKDIR /app

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Install dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Utilisateur non-root et accès
RUN chown appuser /app ; chmod -R 770 /app
USER appuser
