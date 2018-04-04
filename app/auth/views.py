
from flask_restful import Resource
from flask import request

from app.userdir.models import User


all_users = []

class Register(Resource):
    '''User registration Class'''

    @classmethod
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

        user = User(userid, username, password)
        all_users.append(user)

        return {"Message": "User created"}, 201

class Login(Resource):
    '''User login Class'''

    @classmethod
    def post(self):
        if 'username' not in request.json or 'password' not in request.json:
            return {"Message": "Username or password missing"}, 201
        username = request.args.get('username')
        password = request.args.get('password')
        exists = [user for user in all_users if user.username == username
                    and user.password == password]

        if exists:
            #create token hash
            username = request.args.get('username')
            password = request.args.get('password')
            return {"Message": "Welcome, login success"}, 200
        else:
            return {"Message": "Check username or password and try again"}, 404


class Reset(Resource):

    @classmethod
    def post(self):
        if 'username' not in request.json or 'new_password' not in request.json:
            return {"Message": "Make sure to fill all required fields"}, 404

        username = request.args.get('username')
        password = request.args.get('password')
        user = [user for user in all_users if user.username == username and
                    user.password == password]
        if not user:
            return {"Message": "No user or password found"},201
        all_users.remove(user[0])
        user[0].password = password
        all_users.append(user[0])
        return {"Message": "Reset success"}, 201
