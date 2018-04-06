
from flask_restful import Resource
from flask import request

from app.userdir.models import User
from app.userdir.views import users_list


small_users_list = []
user5 = User(5,'Miguna','pass123')
user6 = User(5,'Mboys','pass123')
user6.active = True
small_users_list.append(user5)
small_users_list.append(user6)
users_list


class Register(Resource):
    '''User registration Class'''

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username'] or not req_data['password']:
            return {"Message": "Username or password missing"}, 400
        username = req_data['username']
        exists = [
            user for user in users_list if user.username == username]

        if exists:
            return {"Message": "Username exists please try another"},409
        userid = 3 #Dummy ID Id will genererated by len(all_user)
        username = req_data['username']
        password = req_data['password']

        user = User(userid, username, password)
        users_list.append(user)

        return {"Message": "User created"}, 201

class Login(Resource):
    '''User login Class'''

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username'] or not req_data['password']:
            return {"Message": "Username or password missing"}, 406
        username = req_data['username']
        password = req_data['password']
        user_items = [user for user in users_list if user.username == username
                    and user.password == password]
        if not user_items:
            return {"Message": "Check username or password and try again"}, 401
        user_items[0].active = True
        return {"Message": "Welcome, login success"}, 202

class Reset(Resource):

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username'] or not req_data['password'] or not req_data['new_password']:
            return {"Message": "Make sure to fill all required fields"}, 400
        username = req_data['username']
        password = req_data['password']
        new_password = req_data['new_password']
        user = [user for user in small_users_list if user.username == username and
                    user.password == password]
        if not user:
            return {"Message": "No user or password found"},201
        small_users_list.remove(user[0])
        user[0].password = new_password
        small_users_list.append(user[0])
        return {"Message": "Reset success"}, 202

class Logout(Resource):

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username']:
            return {"message": "malformed request"}, 406
        username = req_data['username']
        user = [user for user in users_list if user.username == username and
                    user.active == True]
        if not user:
            return {"message": "user unknown"}, 401
        user[0].active = False
        return {"message": "Successfull, You are logged out"}, 200