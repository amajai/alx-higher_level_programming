#!/usr/bin/python3
"""
Module to query the states list from database
"""
import MySQLdb
import sys


def get_state(username, password, database_name, state_name):
    """
    takes in an argument and displays all values in the states.
    """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name
    )
    cursor = db.cursor()
    q = "SELECT * FROM states WHERE name = %s"
    cursor.execute(q, (state_name,))

    res = cursor.fetchall()
    for state in res:
        print(state)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    get_state(username, password, database_name, state_name)
