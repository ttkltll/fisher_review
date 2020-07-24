
import json

from flask import jsonify, request, current_app, make_response, flash, render_template
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection
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


class Wishes(object):
    def __init__(self):
        self.total = 0
        self.trades = []

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 如何拿到这本书的字典？现在有isbn,到api上找到这本书，返回一个
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    # print(__dict__(yushu_book2))
    # 怎么把yushu_book2这个对象转换成所要的数据，能被网页渲染的数据呢？
    book = BookViewModel(yushu_book.first)
    has_in_gifts = current_user.has_in_gift(isbn)
    has_in_wishes = current_user.has_in_wish(isbn)
    # 要显示多少个人想要，还要显示，wishes.trades,这是个关于这本书，所有的wish,列表
    wishes = Wishes()
    wishes.total = Wish.wish_user_total(isbn)
    wishes.trades = Wish.wish_user_list(isbn)

    return render_template('book_detail.html', book=book,wishes=[], gifts=[], wish=[], has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)


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
