
from flask import render_template, request

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel
from . import web




@web.route('/')
def index():
    """
    怎么显示最近上传？上传的都是一些每个作者能赠送的书
    拿到所有礼物的数据
    如何把拿到的wishes转换成书籍的格式？

    :return:
    """
    recent_gifts = Gift.recent() #拿到所有符合条件的礼物，比如不重复。这个事，一个类方法可以实现
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)

@web.route('/personal')
def personal_center():
    pass
