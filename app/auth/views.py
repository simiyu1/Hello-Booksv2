
from flask_restful import Resource
from flask import request

from app.userdir.models import User


all_users = []

class Register(Resource):
    '''User registration Class'''

    def post(self):
        if 'username' not in request.json or 'password' not in request.json:
            return {"Message": "Username or password missing"}, 201
        username = request.args.get('username')
        exists = [
            user for user in all_users if user.username == username]

        if exists:
            return {"Message": "Username exists please try another"}

        userid = 3 #Dummy ID Id will genererated by len(all_user) 
        username = request.args.get('username')
        password = request.args.get('password')
        role = request.args.get('role')

        user = User(userid, username, password, role)
        all_users.append(user)

        return {"Message": "User created"}, 201


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