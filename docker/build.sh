#!/bin/bash

# Make and run migrations (only needs to be run on build)
python3  /tram/src/tram/manage.py makemigrations tram
python3  /tram/src/tram/manage.py migrate

# Create a super user for the Django server
#   This should be set by ENV and must include:
#      - DJANGO_SUPERUSER_USERNAME
#      - DJANGO_SUPERUSER_PASSWORD
#      - DJANGO_SUPERUSER_EMAIL
python3 /tram/src/tram/manage.py createsuperuser --noinput
python3 -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('stopwords')"
python3 /tram/src/tram/manage.py attackdata load
python3 /tram/src/tram/manage.py pipeline load-training-data
python3 /tram/src/tram/manage.py pipeline train --model nb
python3 /tram/src/tram/manage.py pipeline train --model logreg
nohup python3 /tram/src/tram/manage.py pipeline run --model logreg &