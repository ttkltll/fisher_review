import json

from flask import jsonify, request, current_app, make_response, flash, render_template
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.user import User
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import  TradeInfo
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook



@web.route('/book/search/')
def search():
    """
        q :普通关键字 isbn
        page
        ?q=金庸&page=1
    """

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return jsonify(books)
        # return json.dumps(books, default=lambda o: o.__dict__)

    else:
        # return jsonify(form.errors)
        flash('被搜索的关键字不符合要示，请重新输入关键字')
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 如何拿到这本书的字典？现在有isbn,到api上找到这本书，返回一个
    """
    1右上角显示，根据current_user来判断
    2如果这个用户的wish,gift都没有，中间是显示 '赠送此书，加入心愿单',如果用户的wish有，那么只显示"已经加入心愿清单",如果用户的gift有，那么只显示"只赠送".判断这本书是不是在wish里，
    3显示几个人想要，拿到这本书的wish然后可以查到多少人，这是多对多关系的一个功能
    4是显示向他们请求此书，还是向他们赠送此书？根据一个标志来确定，这个跟current_user有关，如果wish中有它，没有wish也没gifts,那么显示"向他们请求"，否则"向他们赠送"。向他们请求，显示这本书的所有gift的用户信息。

    模板中的对象：wishes.total,wishes.trades[gift{user_name,time,id}]，has_in_wishes
     :param isbn:
    :return:
    """
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # MVC MVT

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html',
                           book=book, wishes=trade_wishes_model,
                           gifts=trade_gifts_model, has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)





@web.route('/test1')
def test1():
    print(id(current_app))
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')
    return ''


@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }
    # data['age']
    r1 = {

    }
    flash('hello,qiyue', category='error')
    flash('hello, jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)

