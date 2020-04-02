class BookViewModel(object):

    @classmethod
    def package_single(cls, data, q):
        returned = {
            'books':[],
            'total':0,
            'keywords':q,
        }
        if data:
            returned['total'] = 1
            returned['books'].append(cls.cut_book_data(book) for book in data['books'])

        return returned


    @classmethod
    def package_collection(cls, data, q):
        returned = {
            'books':[],
            'total':0,
            'keywords':q,
        }
        if data:
            returned['books'] = [cls.cut_book_data(book) for book in data['books']]
            returned['total'] = data['total']
        return returned

    @classmethod
    def cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }

        return book

