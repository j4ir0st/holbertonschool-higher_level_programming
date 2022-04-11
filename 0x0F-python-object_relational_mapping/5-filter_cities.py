#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT cities.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """, (argv[4], ))
    pr = cur.fetchall()
    print(*[row[0] for row in pr], sep=", ")
