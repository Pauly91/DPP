from flask import Flask
from flask_restful import Resource, Api
from flask import request, jsonify

from app.DPLayer.smartNoiseDP import SmartNoiseDP
from app.configuration.connector import getConfiguration
from app.utils.sqlParser import SQLParser


class queryHandler(Resource):
    def __init__(self):
        config = getConfiguration()
        self.dpLayer = SmartNoiseDP(config)
        self.sqlParser = SQLParser(config['privacy']['whitelist'])

    def get(self):

        json_data = request.get_json(force=True)
        query = json_data['query']

        try:
            self.sqlParser.parse(query)
        except Exception as e:
            return jsonify(e.args)

        return jsonify(self.dpLayer.executeQuery(query))


app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')
app.config.from_object('config')

api = Api(app)
api.add_resource(queryHandler, '/')


'''
curl -d '{"query":"SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married"}' -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/
'''
