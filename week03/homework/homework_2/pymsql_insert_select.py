#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""作业2
姓名: 邓钦元

要求如下:
(1)使用sqlalchemy ORM方式创建如下表，使用PyMySQL对该表写入3条测试数据，并读取:
- 用户id, 用户名, 年龄, 生日, 性别, 学历, 字段创建时间, 字段更新时间
"""
import sys
sys.path.append("/home/secwalker/gitProjects/Python005-01/week03/")
from homework import db_config
import pymysql




def execute_sql_insert(db_config: dict) -> None:
    """
    Insert data to database 
    """
    # connect database
    db = pymysql.connect(**db_config)

    # execute sql statement
    try:
        with db.cursor() as cursor:
            insert_sql = "INSERT INTO user (username, age, birthday, gender, qualification) " \
                "VALUES (%s, %s, %s, %s, %s)"
            values = (
                ('张三', 15, '2014-12-23', '男', '大学'),
                ('李四', 16, '2015-3-21', '女', '大专'),
                ('王五', 19, '2012-12-12', '女', '高中')
            )
            cursor.executemany(insert_sql, values)

        db.commit()

    except Exception as e:
        print(f"fetch error {e}")

    # close database connection
    finally:
        db.close()


def execute_sql_query(db_config: dict) -> None:
    """
    Query data from database 
    """
    # connect database
    db = pymysql.connect(**db_config)

    # execute sql statement
    try:
        with db.cursor() as cursor:
            query_sql = "SELECT username,age FROM user"
            cursor.execute(query_sql)
            result = cursor.fetchall()
            print(result)

        db.commit()

    except Exception as e:
        print(f"fetch error {e}")

    # close database connection
    finally:
        db.close()


if __name__ == "__main__":
    # read database configuration
    db_server = db_config.read_db_config()

    # connect database and insert data
    execute_sql_insert(db_server)

    # connect database and query data
    execute_sql_query(db_server)
