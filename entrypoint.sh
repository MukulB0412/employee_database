#!/bin/sh

echo "⏳ Waiting for Postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "✅ Postgres is up"

python manage.py migrate
python manage.py seed_data

exec "$@"
