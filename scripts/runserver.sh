#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

if [ $ENV = "LOCAL" ]
then
  echo "💻 AMBIENTE LOCAL IDENTIFICADO."
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
    sleep 2
  done

  echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"
else
  echo "⛅ AMBIENTE DE PRODUÇÃO IDENTIFICADO."
fi

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:$PORT