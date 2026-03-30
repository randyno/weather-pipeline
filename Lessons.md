## Dockers
### Dockerfile
Don't use a ubuntu image for the three micro services. It will be too heavy to build.
  Instead use a python image each time. It is more simple and things will go smoothly 
### Micro-services
- weather-db : get data from the API and load it in ./data/raw
Differents enjeux : 
    * "Run once" VS "Run always" : si get_data_from_api.py s'arrete apres avoir telecharge les donnees--> Docker pense que container s'arrete (`restart: no`)
    si get_data_from_api.py doit continuellement charger les donnees dans les raw `restart: always` (ideal pour les bdd et les dashboards)
    * Les permissions utilisateurs : le docker tourne en tant que `root` et les fichiers crees ne sont exploitables que par un autre utilisateur `root`. Que se passe-t-il lorsqu'on essayera de lire ou de supprimer les fichiers depuis le systeme l'ordinateur (windows/MAC) en utilisateur normal ?
