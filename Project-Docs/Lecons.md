## Dockers
### Dockerfile
Don't use a ubuntu image for the three micro services. It will be too heavy to build.
  Instead use a python image each time. It is more simple and things will go smoothly 
### Micro-services
    * "Run once" VS "Run always" : si get_data_from_api.py s'arrete apres avoir telecharge les donnees--> Docker pense que container s'arrete (`restart: no`)
    si get_data_from_api.py doit continuellement charger les donnees dans les raw `restart: always` (ideal pour les bdd et les dashboards)
    * Les permissions utilisateurs : le docker tourne en tant que `root` et les fichiers crees ne sont exploitables que par un autre utilisateur `root`. Que se passe-t-il lorsqu'on essayera de lire ou de supprimer les fichiers depuis le systeme l'ordinateur (windows/MAC) en utilisateur normal ?

    * surcharge du `Dockerfile` et de `requirements.txt` On se rend compte que chaque micro-service est assez different des autres et exploite des dependences uniques. Importer tant de librairies python dans l'image va la rendre trop lourde. La solution serait donc d'avoir pour chaque micro-service son propre Dockerfile et ses propres librairies python.

## DBT
  - `dbt init` cree un nouveau projet avec les different repertoires a personaliser.
  Il est essentiel de preciser la localisation du fichier `profiles.yml` a dbt sinon, il va le chercher dans ~/.dbt/

## GitHub Actions 
  - Chaque job dans les workflow s'execute sur un serveur separe. Une fois l'execution terminee, le serveur est detruit.
  - `needs` ne permet de transmettre les parametres entre serveurs de jobs differents. Il permet seulement d'organiser chronologiquement les jobs