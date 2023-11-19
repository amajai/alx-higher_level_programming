#!/usr/bin/python3
"""
Module to query the states list from database
"""
import MySQLdb
import sys


def get_cities(username, password, database_name):
    """
    takes in an argument and displays all values in the cities.
    """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name
    )
    cursor = db.cursor()
    q = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(q)

    res = cursor.fetchall()
    for state in res:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    get_cities(username, password, database_name)
