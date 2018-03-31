from app.bookdir.models import Book
from flask_restful import Resource
from flask import request

# Holds all books in the app
books_list = []
book1 = Book(1,'The Eleventh Commandment','Jeffrey Archer','1','Harper Collins',7)
book2 = Book(2,'If Tomorrow Comes','Sidney Sheldon','1','Grand Central Publishers',7)
book3 = Book(3,'Origin','Dan Brown','1','Double Day',7)
book4 = Book(4,'Memory Man','David Baldacci','1','Grand Central Publishers',7)
book5 = Book(5,'A time to kill','John Grisham','1','Harper Collins',7)
book6 = Book(6,'The Pillars of the Earth','Ken Follet','1','Macmillan'7)
book7 = Book(7,'Done Deal','Ken Follet','1','Macmillan',7)
book8 = Book(8,'The outlet and Gober','Ken Follet','1','Macmillan',7)
books_list.append(book1)
books_list.append(book2)
books_list.append(book3)
books_list.append(book4)
books_list.append(book5)
books_list.append(book6)
books_list.append(book7)
books_list.append(book8)
class books(Resource):
    
    def get(self, ISBN = None):
        if ISBN != None:
            items = []
            items = [book for book in books_list if book.ISBN == ISBN]
            if len(items) < 1:
                return 'Item not found', 404
            return ({'Book': {'ISBN': items[0].ISBN, 'title': items[0].title, 'author': items[0].author}}), 200
            
        else:
            items = []
            if len(books_list) < 1:
                return 'Books not found', 404
            for book in books_list:
                items.append({'ISBN': book.ISBN, 'title': book.title, 'author': book.author})
            return (items), 200

    def generateID(self):
        items = [book.ISBN for book in books_list]
        if len(items) == 0:
            return 1
        items.sort()
        newID = items[-1] + 1
        return newID

    def make_response(self, Book):
        data = {'ISBN': Book.ISBN, 'title': Book.title, 'author': Book.author}

        return data

    def post(self, ISBN, title, author, edition, publisher, copies):
        if not request.json or 'author' not in request.json or 'title' not in request.json:
            return {'message':'Missing book details'}

        ISBN = self.generateID()
        title = request.json['title']
        author = request.json['author']
        edition = request.json['edition']
        publisher = request.json['publisher']
        copies = request.json['copies']

        book = Book(self, ISBN, title, author, edition, publisher, copies)
        books_list.append(book)
        data = self.make_response(book)
        return (data), 201

    def books = [book for book in books_list if book.id == id]

        if len(books) < 1:
            return 'Book entry not found', 404
        books_list.remove(books[0])
        return 204

    def make_response(self, Book):
        data = {'id': Book.id, 'title': Book.title, 'author': Book.author}

        return data


    def put(self, ISBN, title, author, edition, publisher, copies):
        if not request.json or 'author' not in request.json or 'title' not in request.json:
            return {'message':'Missing book details'}
        ISBN = request.json['ISBN']
        title = request.json['title']
        author = request.json['author']


        items = [book for book in books_list if book.id == item_id]

        books_list.remove(items[0])

        items[0].ISBN = 3
        items[0].title = title
        items[0].author = author

        books_list.append(items[0])

           
        return ({'id':items[0].id,'title':items[0].title,'author':items[0].author}),200

