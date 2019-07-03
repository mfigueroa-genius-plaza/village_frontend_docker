#!/bin/sh

# install dependencies
cd /code
pipenv install --dev

# wait for postgres container to start

# change to application root
cd /code/application

# run migrations
pipenv run python manage.py migrate

# start dev server for use w/ remote debugger
pipenv run python debug.py runserver 0.0.0.0:8000
