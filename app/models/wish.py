from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship
from flask import current_app
from collections import namedtuple

from app.spider.yushu_book import YuShuBook




class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)

    def wish_user_total(self, isbn):
        return Wish.query.count().filter_by(isbn)

    def wish_user_list(self, isbn):
        return Wish.query.all(isbn)

    def user_name(self, uid):
        user.name