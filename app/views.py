
from flask_restful import Resource, Api


class queryHandler(Resource):
    def get(self):
        return {"hello": "Hello Worldsadas"}


'''
tuts: https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework
'''
