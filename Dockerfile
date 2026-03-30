FROM python:3.10-slim

WORKDIR /app
# Par défaut, quand tu démarres une image Linux (comme Ubuntu), tu te retrouves à la racine (/). 
# La racine contient des dossiers systèmes critiques : /bin, /etc, /var, /usr.
# C'est pourquoi on cree un dossier /app pour eviter de polluer la racine.

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
