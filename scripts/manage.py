import sys
import os
from db.connection import Db

def migratedb(file_path):
    # build conn str
    str = "host='%s' dbname='%s' user='%s' password='%s' port='%s'"%(os.environ.get("DB_HOST"), os.environ.get("DB_NAME"), os.environ.get("DB_USER"), os.environ.get("DB_PASSWORD"), os.environ.get("DB_PORT"))
    db = Db(str)
    db.connect()
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    for line in lines:
        if len(line.strip()) != 0:
            db.execute(line.strip("\n"))
    db.disconnect()
    return


def main():

    
    if sys.argv[1] == "migrate_db":
        migratedb(os.environ.get("DB_SCHEMA") + "/tables_up.sql")
    elif sys.argv[1] == "migrate_data":    
        migratedb(os.environ.get("DB_SCHEMA") + "/load_users.sql")
    elif sys.argv[1] == "teardown":   
        migratedb(os.environ.get("DB_SCHEMA") + "/tables_down.sql")
    return

if __name__ == "__main__":
    main()        