from . import web
from flask import render_template


__author__ = '七月'


class Change(object):
    def __init__(self, gift):
        self.title = gift.book.title
        self.author = gift.book.author
        self.summary = gift.book.summary

@web.route('/')
def index():
    # 这个recent是个列表，里面是最新的gift
    gifts = Gift.
    recent = [Change(x) for x in gifts]
    return render_template('index.html', recent=[])

@web.route('/personal')
def personal_center():
    pass
