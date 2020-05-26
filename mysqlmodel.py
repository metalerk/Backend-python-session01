#!/usr/bin/env python

"""
This module performs database operations to MariaDB
"""

from mysql.connector import (
    connect,
    Error,
)

# Connection data to db
DB = {
    'database': 'Biblioteca',
    'host': 'localhost',
    'user': 'Biblioteca',
    'port': 3306,
    'password': 'Biblioteca', # trailing comma
}

def connect_db():
    """
    Connects to db. Return connection or None in case of error.
    """
    try:
        conn = connect(**DB)
    except Error as err:
        print(err)
        return None
    
    return conn

def get_registries(table):
    """
    Gets a list of registries from table and returns in a list.
    """
    # Connection to db
    conn = connect_db()
    if conn:
        # cursor
        cur = conn.cursor()
        sql = "SELECT * FROM {}".format(table)
        cur.execute(sql)
        registries = [[r[0].capitalize() for r in cur.description]]
        registries += cur.fetchall()
        conn.close()

        return registries
    else:
        return []

def get_tables():
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        sql = 'SHOW TABLES'
        cur.execute(sql)
        registries = cur.fetchall()
        conn.close()

        return registries
    else:
        return [] 
