from flask import render_template

from app import app

@app.route('/')
def index():
    return "Hello World"





'''
tuts: https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework
'''