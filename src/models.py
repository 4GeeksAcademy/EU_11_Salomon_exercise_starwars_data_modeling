import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    e_mail = Column(String(250))
    address = Column(String(250))

class Account(Base):
    __tablename__ = 'account'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user.id'))
    username= Column(String(250))
    password = Column(String(250))
    id = Column(Integer, primary_key=True)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user_id.id'))
    character = Column(String(250))
    planets = Column(String(250))
    vehicles = Column(String(250))
    id = Column(Integer, primary_key=True)

class Rating(Base):
    __tablename__ = 'rating'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user_id.id'))
    rating_id = Column(String(250))
    post_id = Column(String(250))
    rating_value = Column(String(250))
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
