#!/bin/sh

sudo pip install -r requirements.txt
python manage.py syncdb --noinput
python manage.py migrate
python manage.py createsuperuser
