import json

from flask import jsonify, request, current_app

from app.forms.book import SearchForm
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
    books = BookCollection()  # 新建一个books对象，这个对象有keyword,books列表，total属性，就是模板要的属性。

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook() # 新建一个yushu_book对象 ，现在它的状态是空的

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q) #调用yushu__book对象的search_by_isbn方法，它会用拿到的数据赶写对象的状态
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)# 调用方法，写入books各个状态
        # return jsonify(books)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)


@web.route('/')
def index():
    args_value  = request.args
    print(args_value)
    return 'hello'

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
