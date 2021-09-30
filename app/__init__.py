

from flask import Flask
from flask_restful import Api
from app.views import queryHandler

app = Flask(__name__, instance_relative_config=True)

# app.config.from_pyfile('config.py')
app.config.from_object('config')

api = Api(app)
api.add_resource(queryHandler, '/')
