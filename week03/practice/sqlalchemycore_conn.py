#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create table by using sqlalchemycore
date: 2020.12.07
"""

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# The first step: create a engine object
# echo=True means open debug option
engine = create_engine("mysql+pymysql://testuser:testpass@localhost:3306/testdb", echo=True)

# The second step: create Metadata object
metadata = MetaData(engine)

# The Third step: create Table object
book_table = Table('book', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )
author_table = Table('author', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_id', None, ForeignKey('book.id')),
    Column('author_name', String(128), nullable=False),
    )

# The fourth step: Start create table
try:
    metadata.create_all()
except Exception as e:
    print(f"create error {e}")
