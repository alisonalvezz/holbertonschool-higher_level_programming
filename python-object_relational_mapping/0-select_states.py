#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def states(username, password, db_name):
    """
    Connects to a MySQL database and retrieves all states by executing a query

    Args:
        username (str): the username for the db connection
        password (str): the password for the db connection
        db_name (str): the database name to connect to
    """

    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,  # Correct parameter name
        db=db_name  # Correct parameter name
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()


if __name__ == "__main__":  # Correct indentation
    user = sys.argv[1]
    passwd = sys.argv[2]  # Use a different name to avoid confusion with the password keyword
    db_name = sys.argv[3]

    states(user, passwd, db_name)
