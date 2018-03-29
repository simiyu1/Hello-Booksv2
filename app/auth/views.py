
from flask_restful import Resource
from flask import request

from app.userdir.user import User


all_users = []

class Register(Resource):
    '''A class to handle the creation of a new user'''

    def post(self):
        if 'username' not in request.json or 'password' not in request.json:
            return {"Message": "Username or password missing"}, 201
        username = request.json['username']
        unavailable = [
            user for user in all_users if user.username == username]

        if unavailable:
            return {"Message": "Username exists please try another"}

        username = request.json['username']
        password = request.json['password']

        user = User(username, password)
        all_users.append(user)

        return {'user details': {'username': user.username, 'borrowings': user.borrowed_books}}, 201


class Reset(Resource):

    def post(self):
        if 'username' not in request.json or 'new_password' not in request.json:
            return {"Message": "Make sure to fill all required fields"}

        username = request.json['username']
        password = request.json['new_password']
        user = [user for user in all_users if user.username == username]
        if not user:
            return {"Message": "No user found with that username"}

        all_users.remove(user[0])
        user[0].password = password
        all_users.append(user[0])

        return {"username": user[0].username, "password": user[0].password}, 201
