# Blueprint names
from app.bookdir import book
from app.userdir import user
from app.auth import auth

from app import app

# Register the blueprints
app.register_blueprint(book)
app.register_blueprint(user)
app.register_blueprint(auth)
#adding the config

if __name__ == '__main__':
    app.run(debug =True)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'This Method is not allowed'}), 405)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Thhis URL is broken, please check and try again '}), 405)
    