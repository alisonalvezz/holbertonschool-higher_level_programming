#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def states(username, password, db_name):
    """
    Connects to a MySQL database and executes a query to
    retrieve all states starting with N

    Args:
        username (str): the username for the db connection
        password (str): the password for the db connection
        db_name (str): the name of the database to make the connection
    """

    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE" +
                   "'N%' ORDER BY states.id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    database.close()


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    states(user, passwd, db_name)
