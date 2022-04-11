#!/usr/bin/python3
from sys import argv
import MySQLdb
db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=argv[1],
                     passwd=argv[2],
                     db=argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states")
pr = cur.fetchall()
for row in pr:
    print(row)
