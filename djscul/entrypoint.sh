#! /bin/bash

# --no-input - мы не получим информацию в консоли

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

# Запускаем программу с gunicorn
exec gunicorn django4life.wsgi:application -b 0.0.0.0:8008 --reload
