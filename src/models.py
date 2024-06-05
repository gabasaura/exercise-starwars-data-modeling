import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    admin_id = Column(Integer, ForeignKey('admin.id'))
    admin = relationship(Admin)

class Favorite(Base):
    __tablename__ = 'favorite'
    user_favorites = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    media_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    media_id = Column(Integer, ForeignKey('media.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    media = relationship(Media)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
