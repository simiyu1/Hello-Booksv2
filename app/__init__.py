from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Very_long_secret_word'
