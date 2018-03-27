
from flask_api import FlaskAPI
from flask import request, jsonify, abort


# local import configs and routes(route file merged here)
from instance.config import app_config






def create_app(config_name):
    from v1.book import Book
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app_config[config_name].init_app(app)

    @app.route('/api/books/', methods=['POST', 'GET'])
    def booklist():
        """Adds a book to the library if POST, or retrieves all books if GET is used"""

        if request.method == "POST":
            isbn = str(request.data.get('ISBN', ''))
            if isbn:
                booklist = Book(ISBN=isbn)
                booklist.save()
                response = jsonify({
                    'ISBN': booklist.ISBN,
                    'title': booklist.title,
                    'author': booklist.author,
                    'edition': booklist.edition,
                    'publisher': booklist.publisher,
                    'copies': booklist.copies
                })
                response.status_code = 201
                return response

        else:
            booklists = Booklist.get_all()
            results = []

            for booklist in booklists:
                obj = {
                    'isbn': booklist.isbn,
                    'title': booklist.title,
                    'author': booklist.author,
                    'edition': booklist.edition,
                    'publisher': booklist.publisher,
                    'copies': booklist.copies
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    
    @app.route('/api/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def booklist_manipulation(isbn, **kwargs):
     # access a single book using it's ISBN
        booklist = get_book_by_isbn(isbn).first()
        if not booklist:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            booklist.delete()
            return {
            "message": "booklist {} entry deleted successfully".format(booklist.isbn) 
         }, 200

        elif request.method == 'PUT':
            isbn = str(request.data.get('isbn', ''))
            booklist.isbn = isbn
            booklist.save()
            response = jsonify({
                'isbn': booklist.isbn,
                    'title': booklist.title,
                    'author': booklist.author,
                    'edition': booklist.edition,
                    'publisher': booklist.publisher,
                    'copies': booklist.copies
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'isbn': booklist.isbn,
                    'title': booklist.title,
                    'author': booklist.author,
                    'edition': booklist.edition,
                    'publisher': booklist.publisher,
                    'copies': booklist.copies
            })
            response.status_code = 200
            return response


    return app

