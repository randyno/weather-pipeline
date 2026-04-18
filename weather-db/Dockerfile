FROM python:3.10-slim

WORKDIR /app

# Creer un utilisateur systeme et son group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copier les fichiers importants
COPY --chown=appuser:appgroup . .

# Installer les dependances en tant que root
RUN pip install --no-cache-dir -r ./requirements.txt

# Se connecter en appuser
USER appuser

EXPOSE 5000
