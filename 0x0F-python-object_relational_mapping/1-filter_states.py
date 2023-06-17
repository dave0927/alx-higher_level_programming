#!/usr/bin/python3
'''
get all states module
'''


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost')
    cur = db.cursor()

    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
