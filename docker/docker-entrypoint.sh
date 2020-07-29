#!/bin/bash

###### Add User to the passwd, if the uid is not the default one ######
echo "Adding UID to temporary passwd"
export USER_ID=$(id -u)
envsubst < /pnp-manager/docker/passwd.template > /pnp-manager/docker/passwd
echo "Finished Adding UID to temporary passwd"


###### Wait for postgres to start ######
function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$DJANGO_DB_NAME", user="$DJANGO_DB_USER", password="$DJANGO_DB_PASSWORD", host="$DJANGO_DB_HOST")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."


###### Collect static files ######
echo "Collect static files"
python manage.py collectstatic --noinput

###### Apply database migrations ######
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

###### Create superuser ######
echo "Creating initial Superuser with Username: $DJANGO_SUPERUSER_ADMIN and Email $DJANGO_SUPERUSER_EMAIL"
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_ADMIN --email $DJANGO_SUPERUSER_EMAIL

###### Start server ######
echo "Starting server"
python manage.py runserver 0.0.0.0:8000