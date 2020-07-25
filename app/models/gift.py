
from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship
from flask import current_app
from collections import namedtuple

from app.spider.yushu_book import YuShuBook




class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)

    @property # 有什么作用呢？除了写属性方便之外。
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(launched=False).group_by(Gift.isbn).limit(current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
