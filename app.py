from flask import Flask
import psycopg2
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
