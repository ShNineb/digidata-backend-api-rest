## Techniques Web INALCO, M2S2 2021

Mise en place d'un environnement de développement web, d'une application Back-End (REST API via méthodes HTTP) avec la librairie Python Flask pour exploiter et déploiement de cette application sur Heroku 


## Organisation interne 

L'applications Back-end utilise la librairie Python Flask. 

- le dossier **resources/**: les resources scripts concernant cette application
- le dossier **data/**: les fichiers de données
- le dossier **utils/**: les script Python pour traiter les tableaux dans le base de données db.sqlite
- le fichier **requirements**: les dépendances logicielles du projet
- le fichier **client.py**: pour lancer l'application

## Installation

Configurer l'environnement de développement avec **virtualenv**. Se rendre dans le dossier principal et éxécuter les commandes: 

    $ pip install virtualenv
	$ virtualenv env
	$ source env/bin/activate
	(env) $ pip install -r requirements.txt
	(env) $ pip install gunicorn

## Utilisation

L'application Back-end fonctionne sous l'URL digidata.api.localhost. 
On le lance avec le fichier `client.py`. 

    python3 client.py

