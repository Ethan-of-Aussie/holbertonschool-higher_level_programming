#!/usr/bin/python3
"""Lists all cities from the database."""

import MySQLdb, sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    query = "SELECT cities.id, cities.name, states.name \
    FROM cities \
    JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC"

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
