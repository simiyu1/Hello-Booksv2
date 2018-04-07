
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


class Register(Resource):
    '''User registration Class'''

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username'] or not req_data['password']:
            return {"message": "username or password missing"}, 400
        username = req_data['username']
        exists = [
            user for user in users_list if user.username == username]

        if exists:
            return {"message": "username exists please try another"},409
        #userid = 3 #Dummy ID Id will genererated by len(all_user)
        userid = len(users_list)+1
        username = req_data['username']
        password = req_data['password']

        user = User(userid, username, password)
        users_list.append(user)

        return {"message": "user created"}, 201

class Login(Resource):
    '''User login Class'''

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username'] or not req_data['password']:
            return {"message": "username or password missing"}, 406
        username = req_data['username']
        password = req_data['password']
        user_items = [user for user in users_list if user.username == username
                    and user.password == password]
        if not user_items:
            return {"message": "check username or password and try again"}, 401
        user_items[0].active = True
        return {"message": "welcome, login success"}, 202

class Reset(Resource):

    @classmethod
    def post(self):
        req_data = request.get_json()
        if not req_data['username'] or not req_data['password'] or not req_data['new_password']:
            return {"message": "make sure to fill all required fields"}, 400
        username = req_data['username']
        password = req_data['password']
        new_password = req_data['new_password']
        user = [user for user in users_list if user.username == username and
                    user.password == password]
        if not user:
            return {"message": "no user or password found"},201
        users_list.remove(user[0])
        user[0].password = new_password
        users_list.append(user[0])
        return {"message": "reset success"}, 202

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
        return {"message": "successfull, You are logged out"}, 200