#!/usr/bin/python3
"""Build the query to take in argv-4 as input to search a state."""

import MySQLdb, sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
