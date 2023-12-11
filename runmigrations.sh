#!/bin/bash


source ./env.sh


if [[ -z "$DB_USER" ]]
then
  echo "Missing $DB_USER"
  exit -1
fi

echo "Creating db"
docker exec $DB_CONTAINER psql -U postgres -c "DROP DATABASE IF EXISTS $DB_NAME;"

docker exec $DB_CONTAINER psql -U postgres -c "CREATE DATABASE $DB_NAME;"

echo "Migrate db"
python ./manage.py migrate_db
python ./manage.py migrate_data


