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
class Book(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author= ','.join(book['author'])
        self.price = book['price']
        self.summary = book['summary']

class BookViewModel(object):
    def __init__(self, data, q):
        self.books = []
        # keywords 从哪来呢
        self.keywords =q
        self.append(data)
        self.total = len(self.books)

    def append(self,data):
        self.books = self.package(data)


    def package(self, result):
        if result['count']:
            return [Book(book) for book in result['books']]
        else:
            return [Book(result)]




