#!/usr/bin/python3
"""
Module to query the states list from database
"""
import MySQLdb
import sys


def get_city_with_state(username, password, database_name, state_name):
    """
    takes in an argument and displays all values in the states.
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
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(q, (state_name,))

    res = cursor.fetchall()
    states = []
    for city in res:
        states.append(city[1])
    print(', '.join(states))
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    get_city_with_state(username, password, database_name, state_name)
