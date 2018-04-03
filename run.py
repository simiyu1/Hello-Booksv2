# Blueprint names
from app.bookdir import book
from app.userdir import user
from app.auth import auth

# from flask import Flask
import app
app = app.app

# Register the blueprints
app.register_blueprint(book)
app.register_blueprint(user)
app.register_blueprint(auth)
@app.route("/", methods =['GET'])
def home():
    return "Hello world"
#adding the config

if __name__ == '__main__':
    app.run(debug =True)