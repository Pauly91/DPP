from flask import render_template
from flask_restful import Resource, Api

from app import app

api = Api(app)


class TodoSimple(Resource):
    def get(self):
        return {"hello": "Hello Worldsadas"}


api.add_resource(TodoSimple, '/')

'''
tuts: https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework
'''
