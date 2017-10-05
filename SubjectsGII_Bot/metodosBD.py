import MySQLdb
import os
import urlparse

db = os.environ["NAME_BD"]
host_db = os.environ["HOST_BD"]
usuario = os.environ["USER_BD"]
pw = os.environ["PW_BD"]

def nombreAsignatura(nombAsig):
    connect_db = MySQLdb.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute(nombAsig)

    num_asig = len(cursor.fetchall())

    if num_asig != 0:
        return True

    connect_db.close()

    return False
