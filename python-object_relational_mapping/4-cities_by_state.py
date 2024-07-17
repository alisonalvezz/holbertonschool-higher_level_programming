#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def states(username, password, db_name):
    """
    Lists all cities from database

    Args:
        username(str): username to connect to the db
        password(str): password to connect to the db
        db_name(str): name of the database
    """

    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = database.cursor()

    query = ("SELECT cities.id, cities.name, states.name " +
                   "FROM cities INNER JOIN states " +
                   "ON cities.state_id = state_id " +
                   "ORDER BY cities.id")
    
    cursor.execute(query)

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