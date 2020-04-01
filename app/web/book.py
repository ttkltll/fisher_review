import json

from flask import jsonify, request, current_app

from app.forms.book import SearchForm
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


#class Book(object):
#    def __init__(self, book):
#        self.title = book['title']
#        self.publisher = book['publisheri']
#        self.pages = book['pages']
#        self.author= book['authoor']
#        self.price = book['price']
#        self.summary = book['summary']

#class BookViewModel(object):
#    def __init__(self, result, q):
#        self.books = []
#        self.total = len(self.books)
#        # keywords 从哪来呢
#        self.keywords =q
#        self.append(result)
#
#    def append(self, result):
#        if result.total:
#            return Book(book) for book in result.books
#        else:
#            return Book(book) for book in result


@web.route('/book/search/')
def search():
    """

    :param q: 普通关键字，isbn
    :param page:
    :return:
    """
    # alt+enter:导入模块
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q, page)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        #result = BookViewModel(result)
        #return jsonify(result)
        return json.dumps(result), 200, {'content-type': 'application/json'}
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
