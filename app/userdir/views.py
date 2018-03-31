from flask_restful import Resource
from flask import request, jsonify
from flask import json

from app.bookdir.views import books_list
from app.userdir.models import User
from app.bookdir.models import Book

# Create dummy users dataset to hold dummy users
users_list = []
user1 = User(1,'Mainmuna Swazi','pass123','client')
user2 = User(2,'Mwenda Nduthi','pass123','client')
user3 = User(3,'Khololosia Mbi','pass123','client')
user4 = User(4,'Kinde Kinde','pass123','client')
users_list.append(user1)
users_list.append(user2)
users_list.append(user3)
users_list.append(user4)
borrowed_books = []
book1 = Book(1,'The Eleventh Commandment','Jeffrey Archer','1','Harper Collins',7)
book2 = Book(2,'If Tomorrow Comes','Sidney Sheldon','1','Grand Central Publishers',7)
borrowed_books.append(book1)
borrowed_books.append(book2)

class Users(Resource):

    def get(self, userid=None):

        senID = request.args.get('userid')

        if senID != None:
            senID = int(senID)
            items = []
            items = [user for user in users_list if user.userid == senID]
            if len(items) < 1:
                return 'User not found', 404
            return ({'username': items[0].username},
                     {'message': 'Welcome to Hello-Books.'}), 200
            
        else:
            items = []
            if len(users_list) < 1:
                return 'Users not found', 404
            for user in users_list:
                items.append({'userid': user.userid, 'username': user.username})
            return (items), 200

        return {'message': 'Welcome to Hello-Books. '}, 200


class Borrow(Resource):

    def post(self, ISBN=None):
        sentISBN = request.args.get('ISBN')
        borrowed = []
        if sentISBN == None:
            return 'You Have to specify the book ISBN',200
        if len(books_list) < 1: #Chec if there are books in the library
            return {"Message":"No Books in the library"}, 404
        item_id = int(sentISBN)
        book = [item for item in books_list if item.ISBN == item_id ]

        if not book:
            return {"Message": "No book found with the given book id"}, 404
        borrowed.append({'ISBN': book[0].ISBN, 'title': book[0].title, 'author': book[0].author})
        #Add to the users list of books
        borrowed_books.append(borrowed)
        #return the book to be checked out
        return (borrowed), 200
