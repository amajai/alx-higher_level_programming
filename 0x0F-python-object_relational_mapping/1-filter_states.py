#!/usr/bin/python3
"""
Module to query the states list from database
"""
import MySQLdb
import sys


def get_states_with_N(username, password, database_name):
    """
    Get the list of states for database
    """
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database_name
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    res = cursor.fetchall()
    for state in res[:2]:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit()
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    get_states_with_N(username, password, database_name)
