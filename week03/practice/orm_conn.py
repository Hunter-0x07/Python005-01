#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create table by using orm
date: 2020.12.07 10:17
"""

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# The first step: create base object
Base = declarative_base()


# The second step: create table class
class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)


class Author(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now())
    updated_on = Column(DateTime(), default=datetime.now(),
                        onupdate=datetime.now())


# The third step: create a engine object
dburl = "mysql+pymysql://testuser:testpass@localhost:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# The fouth step: start create table
Base.metadata.create_all(engine)
