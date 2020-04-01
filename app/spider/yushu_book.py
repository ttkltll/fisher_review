from flask import current_app

from app.libs.httper import HTTP

__author__ = '谭亮'


class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'


    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        start = (page-1)*current_app.config['PER_PAGE']+1
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], start)
        result = HTTP.get(url)
        return result
