#class BookViewModel(object):
#
#    @classmethod
#    def package_single(cls, data, q):
#        returned = {
#            'books':[],
#            'total':0,
#            'keywords':q,
#        }
#        if data:
#            returned['total'] = 1
#            returned['books'].append(cls.cut_book_data(book) for book in data['books'])
#
#        return returned
#
#
#    @classmethod
#    def package_collection(cls, data, q):
#        returned = {
#            'books':[],
#            'total':0,
#            'keywords':q,
#        }
#        if data:
#            returned['books'] = [cls.cut_book_data(book) for book in data['books']]
#            returned['total'] = data['total']
#        return returned
#
#    @classmethod
#    def cut_book_data(cls, data):
#        book = {
#            'title': data['title'],
#            'publisher': data['publisher'],
#            'pages': data['pages'] or '',
#            'author': '、'.join(data['author']),
#            'price': data['price'],
#            'summary': data['summary'] or '',
#            'image': data['image']
#        }
#
#        return book
#
#class Book(object):
#    def __init__(self, book):
#        self.title = book['title']
#        self.publisher = book['publisher']
#        self.pages = book['pages']
#        self.author= ','.join(book['author'])
#        self.price = book['price']
#        self.summary = book['summary']
#
#class BookViewModel(object):
#    def __init__(self, data, q):
#        self.books = []
#        # keywords 从哪来呢
#        self.keywords =q
#        self.append(data)
#        self.total = len(self.books)
#
#    def append(self,data):
#        self.books = self.package(data)
#
#
#    def package(self, result):
#        if result['count']:
#            return [Book(book) for book in result['books']]
#        else:
#            return [Book(result)]



class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']

    @property
    def intro(self):
        #return self.title + '/' + self.publisher + '/ $' + self.price
    # 这种处理不好，如果self.publisher没有数据，就变成中间两条//,
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)
        # 怎么加上符号呢？



class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

