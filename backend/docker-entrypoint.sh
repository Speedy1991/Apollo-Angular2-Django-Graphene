#!/usr/bin/env bash

sleep 5 # Sleep for starting db

echo "Make Migrations"
python manage.py makemigrations

echo "Migrate"
python manage.py migrate

python manage.py sqlflush
python manage.py sqlflush | python manage.py dbshell
python manage.py flush --no-input

echo "Load dummy data"
python manage.py loaddata init

echo "Start server"
python manage.py runserver