from flask import Flask, jsonify, make_response
app = Flask(__name__)
app.url_map.strict_slashes = False


app.config['SECRET_KEY'] = 'Very_long_secret_word'
@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify({'error': 'This Method is not allowed'}), 405)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'This URL is broken, please check and try again '}), 404)
  
