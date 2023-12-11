#!/bin/bash


source ./env.sh
source ./migratedb.sh


echo "Run tests"
pytest test_user.py -v
echo "Teardown db"
python ./manage.py teardown

