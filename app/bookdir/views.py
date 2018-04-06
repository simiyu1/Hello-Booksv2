from flask_restful import Resource
from flask import request
from app.bookdir.models import Book


#Dummy dataset to hold all books in the app
books_list = []
book1 = Book(1,'The Eleventh Commandment','Jeffrey Archer')
book2 = Book(2,'If Tomorrow Comes','Sidney Sheldon')
book3 = Book(3,'Origin','Dan Brown')
book4 = Book(4,'Memory Man','David Baldacci')
book5 = Book(5,'A time to kill','John Grisham')
book6 = Book(6,'The Pillars of the Earth','Ken Follet')
book7 = Book(7,'Done Deal','Ken Follet')
book8 = Book(8,'The outlet and Gober','Ken Follet')
books_list.append(book1)
books_list.append(book2)
books_list.append(book3)
books_list.append(book4)
books_list.append(book5)
books_list.append(book6)
books_list.append(book7)
books_list.append(book8)

class books(Resource):
    @classmethod
    def get(self, ISBN=None):
        if ISBN != None:
            items = []
            items = [book for book in books_list if book.ISBN == int(ISBN)]
            if len(items) < 1:
                return 'Item not found', 404
            return ({'Book': {'ISBN': items[0].ISBN, 'title': items[0].title, 'author': items[0].author}},{'message':'Gets a specific book'}), 200
        else:
            manyitems = []
            if len(books_list) < 1:
                return 'Books not found', 404
            for book in books_list:
                manyitems.append(
                    {'ISBN': book.ISBN, 'title': book.title, 'author': book.author})
            return manyitems, 200

    @classmethod
    def make_response(self, Book):
        data = {'ISBN': Book.ISBN, 'title': Book.title, 'author': Book.author}
        return data, 200

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['author']:
            return {'message':'Missing book details'}, 404
        New_ID = len(books_list) #
        ISBN = New_ID
        title = req_data['title']
        author = req_data['author']
        newbook = Book(ISBN, title, author)
        books_list.append(newbook)
        return ({'msg':'book added'}), 201

    @classmethod
    def delete(self, ISBN=None):
        if ISBN ==None:
            return "Book ID expected", 406
        books = [book for book in books_list if book.ISBN == int(ISBN)]
        if len(books) < 1:
            return {'message':'book entry not found'}, 404
        books_list.remove(books[0])
        return ({'msg':'book deleted'}),200

    @classmethod
    def put(self):
        req_data = request.get_json()
        if not req_data['ISBN'] or not req_data['title'] or not req_data['author']:
            return {"message": "details missing"}, 406
        else:
            ISBN = req_data['ISBN']
            title = req_data['title']
            author = req_data['author']
            items = [book for book in books_list if book.ISBN == int(ISBN)]
            if not items:
                return {"message":"book to update not found"}, 401
            prev_title = items[0].title
            books_list.remove(items[0])
            items[0].ISBN = ISBN
            items[0].title = title
            items[0].author = author
            books_list.append(items[0])
            return (items[0].title,"Previously", prev_title), 200

