from flask import current_app

from app.libs.httper import HTTP

__author__ = '谭亮'


class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict
        self.total = 1
        self.books.append(result)

    def search_by_keyword(self, keyword, page=1):
        start = (page-1)*current_app.config['PER_PAGE']+1
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], start)
        result = HTTP.get(url)
        self.total = result.total
        self.books = self.package(result)

    def package(self, dict):
        ###完成什么功能呢？ 把result数据，一个字典，转换成一个列表
        list = []
        list = dict.books
        return list
### 我写的问题在哪：1package 没有加__,这个方法显然是私有的，不用让外面知道。2dict.books,改成：dict['books'],3self.list = dict['books']就可以了

