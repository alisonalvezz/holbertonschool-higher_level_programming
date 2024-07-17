#!/usr/bin/python3
import MySQLdb
import sys
"""Write a script that takes in an argument and displays 
all values in the states table of hbtn_0e_0_usa where name matches the argument."""


def states(username, password, db_name, state_name):
    """
    Connects to a MySQL database and executes a query to display
    all values in the states table where name matches the argument

    Args:
        username(str): the username for the db connection
        password(str): the password for the db connection
        db_name(str): the name of the database
        state_name(str): the name of the state
    """

    database = MySQLdb.connect(
        host='localhost', 
        port=3306,
        user=username,
        passwd=password, 
        db=db_name
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id".format(state_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    states(username, password, db_name, state)
