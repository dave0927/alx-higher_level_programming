#!/usr/bin/python3
'''
get all states module
'''

from sys import argv
import MySQLdb


if __name__ == "__main__":
    HOST = 'localhost'
    USER = argv[1]
    PASSWD = argv[2]
    DB = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    cur.execute(""" SELECT * FROM states WHERE
                name='{}' ORDER BY id ASC """.format(argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
