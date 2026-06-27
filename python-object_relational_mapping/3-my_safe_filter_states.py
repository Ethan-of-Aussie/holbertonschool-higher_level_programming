#!/usr/bin/python3
"""Protected from injections due to wildcard string and
arguement in execute placed as a tuple forced by execute."""

import MySQLdb, sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
