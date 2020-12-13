#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Connect to mysql by using pymysql
date: 2020.12.07
preparation: 

# mysql > CREATE DATABASE testdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
# mysql > GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';
"""

import pymysql
from db_config import read_db_config


def execute_sql_query(db_config: dict) -> None:
    """Connect database and execute sql query
    :param: a dictionary of database configuration
    :return: None
    """
    # connect to database
    db = pymysql.connect(**db_config)

    # execute sql query
    try:
        with db.cursor() as cursor:
            sql = "SELECT VERSION()"
            cursor.execute(sql)
            result = cursor.fetchone()
        db.commit()

    except Exception as e:
        print(f"fetch error {e}")

    # close database connection
    finally:
        db.close()

    print(f"Database version {result}")


if __name__ == "__main__":
    # read database configuration
    db_server = read_db_config()

    # connect and execute sql query
    execute_sql_query(db_server)
