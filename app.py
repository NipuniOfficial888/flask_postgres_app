from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, Flask with PostgreSQL!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
