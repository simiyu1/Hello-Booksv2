from flask import Blueprint

book = Blueprint('books', __name__, url_prefix='/api/v1/books/')

from app.bookdir.views import books
from app.bookdir import models

from app import app
from flask_restful import Api

api = Api(app)

api.add_resource(books, '/api/v1/books/', '/api/v1/books/<author>/')
