from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['SECRET_KEY'] = 'Very_long_secret_word'
