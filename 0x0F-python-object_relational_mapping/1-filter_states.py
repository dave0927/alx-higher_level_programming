#!/usr/bin/python3

'''
filter states 
'''

import sys
import MySQLdb

if __name__ == "__main__":
    HOST = 'localhost'
    DB_USER = sys.argv[1]
    DB_PASS = sys.argv[2]
    DB_NAME = sys.argv[3]

    db = MySQLdb.connect(HOST, DB_USER, DB_PASS, DB_NAME)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
