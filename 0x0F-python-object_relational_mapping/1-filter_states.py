#!/usr/bin/python3

'''
filter states
'''

import sys
import MySQLdb

if __name__ == "__main__":
    HOST = 'localhost'
    DBUSER = sys.argv[1]
    DBPASS = sys.argv[2]
    DBNAME = sys.argv[3]
    PORT = 3306

    db = MySQLdb.connect(HOST, PORT, DBUSER, DBPASS, DBNAME)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
