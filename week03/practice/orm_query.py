#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey, desc, func, and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime


Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(book_id='{self.book_id}', " \
            "book_name={self.book_name})".format(self=self)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


# create engine object
db_url = "mysql+pymysql://testuser:testpass@localhost:3306/testdb?charset=utf8mb4"
engine = create_engine(db_url, echo=True, encoding="utf-8")

# create session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# insert data
# book_demo = Book_table(book_name='肖申克的救赎')
# book_demo2 = Book_table(book_name='活着')
# book_demo3 = Book_table(book_name='西游记')

# session.add(book_demo)
# session.add(book_demo2)
# session.add(book_demo3)
# session.commit()

# query data
# result = session.query(Book_table).all()
# for result in session.query(Book_table):
#     print(result)
# result = session.query(Book_table).first()
# result = session.query(Book_table).one()
# result = session.query(Book_table).scalar()
# for result in session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)):
#     # print(result)
#     print(result.book_name)
# query = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(3)
# print([result.book_name for result in query])
# result = session.query(func.count(Book_table.book_name)).all()
# result = session.query(Book_table).filter(Book_table.book_id < 20).first()

# print(result)


# update data
# query = session.query(Book_table)
# query = query.filter(Book_table.book_id == 4)
# query.update({Book_table.book_name: 'newbook'})
# new_book = query.first()
# print(new_book.book_name)

# delete data
# query = session.query(Book_table)
# query = query.filter(Book_table.book_id == 4)
# # session.delete(query.one())
# query.delete()
# print(query.first())

# session.commit()
