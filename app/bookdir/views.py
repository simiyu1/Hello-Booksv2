from app.bookdir.models import Book
from flask_restful import Resource
from flask import request

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
    def get(self, author=None):
        author = request.args.get('author')
        if author != None:
            items = []
            items = [book for book in books_list if book.author == author]
            if len(items) < 1:
                return 'Item not found', 404
            return ({'Book': {'ISBN': items[0].ISBN, 'title': items[0].title, 'author': items[0].author}},{'message':'Gets a specific book'}), 201
        else:
            manyitems = []
            if len(books_list) < 1:
                return 'Books not found', 200
            for book in books_list:
                manyitems.append(
                    {'ISBN': book.ISBN, 'title': book.title, 'author': book.author})
            return manyitems, 200

    def make_response(self, Book):
        data = {'ISBN': Book.ISBN, 'title': Book.title, 'author': Book.author}
        return data

    def post(self):
        if not request.args.get('userid') or 'author' not in request.args.get('author') or 'title' not in request.args.get('title'):
            return {'message':'Missing book details'}
        NewID = len(books_list) #
        ISBN = NewID
        title = request.args.get('title')
        author = request.args.get('author')
        newbook = Book(ISBN, title, author)
        books_list.append(newbook)
        return ({'msg':'Book added'}), 201

    def delete(self):
        ISBN = request.args.get('ISBN')
        print(ISBN)
        books = [book for book in books_list if book.ISBN == ISBN]
        if len(books) < 1:
            return {'Message':'Book entry not found'}, 404
        books_list.remove(books[0])
        return ({'msg':'Book deleted'}),200

    def put(self):
        if not request.args.get('ISBN'):
            return {'message':'Missing book details'}, 201

        else:
            ISBN = request.args.get('ISBN')
            title = request.args.get('title')
            author = request.args.get('author')
            
            items = [book for book in books_list if book.ISBN == ISBN]
            if not items:
                return "Book to update not found"
                
            books_list.remove(items[0])
            items[0].ISBN = ISBN
            items[0].title = title
            items[0].author = author
            
            books_list.append(items[0])
            return (items[0].title),200

