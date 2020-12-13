#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""作业2
姓名: 邓钦元

要求如下:
(1)使用sqlalchemy ORM方式创建如下表，使用PyMySQL对该表写入3条测试数据，并读取:
- 用户id, 用户名, 年龄, 生日, 性别, 学历, 字段创建时间, 字段更新时间
"""
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# The first step: create base object
Base = declarative_base()

# The second step: create table class
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    age = Column(Integer(), nullable=False)
    birthday = Column(Date(), nullable=False)
    gender = Column(String(10), nullable=False)
    qualification = Column(String(10), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

# The third step: create a engine object
db_url = "mysql+pymysql://testuser:testpass@localhost:3306/testdb?charset=utf8mb4"
engine = create_engine(db_url, echo=True, encoding="utf-8")

# The fourth step: start create table 
Base.metadata.create_all(engine)