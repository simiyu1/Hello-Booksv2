from flask_restful import Resource
from flask import request, jsonify
from flask import json

from app.bookdir.views import books_list
from app.userdir.models import User
from app.bookdir.models import Book

# Create dummy users dataset to hold dummy users
users_list = []
user1 = User(1,'Mainmuna Swazi','pass123')
user2 = User(2,'Mwenda Kifikifi','pass123')
user3 = User(3,'Khololosia Mbi','pass123')
user4 = User(4,'Kinde Kinde','pass123')
user5 = User(5,'Miguna','pass123')
users_list.append(user1)
users_list.append(user2)
users_list.append(user3)
users_list.append(user4)
borrowed_books = []
book1 = Book(1,'The Eleventh Commandment','Jeffrey Archer')
book2 = Book(2,'If Tomorrow Comes','Sidney Sheldon')
borrowed_books.append(book1)
borrowed_books.append(book2)

class Users(Resource):

    def get(self, userid=None):

        if request.args.get('userid') != None:
            senID = request.args.get('userid')
            items = []
            items = [user for user in users_list if user.userid == int(senID)]
            if len(items) < 1:
                return 'User not found', 404
            return ({'user':{'userid': items[0].userid, 'username': items[0].username, 'role': items[0].role}}, {'message': 'Fetched User'}), 200
            
            
        else:
            items = []
            if len(users_list) < 1:
                return 'Users not found', 404
            for user in users_list:
                items.append({'userid': user.userid, 'username': user.username})
            #return (items), 200
            size = len(items)
            return ({'username': items[0].username},
                     {'message': 'Fetched User'}), 200

        


class Borrow(Resource):

    def post(self, ISBN=None):
        sentISBN = request.args.get('ISBN')
        borrowed = []
        if sentISBN == None:
            return 'You Have to specify the book ISBN',200
        if len(books_list) < 1: #Chec if there are books in the library
            return {"Message":"No Books in the library"}, 404
        else:
            item_id = int(sentISBN)
            book = [item for item in books_list if item.ISBN == item_id ]
            if not book:
                return {"Message": "No book found with the given book id"}, 404
            else:
                borrowed.append({'ISBN': book[0].ISBN, 'title': book[0].title, 'author': book[0].author})
                borrowed_books.append(borrowed)
            return ({'Message': 'Book borrowed'}), 200
