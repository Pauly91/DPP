from flask import Flask
from flask_restful import Resource, Api
from flask import request, jsonify

from app.DPLayer.SmartNoise.smartNoiseDP import SmartNoiseDP
from app.configuration.connector import getConfiguration
from app.utils.sqlParser import SQLParser

config = getConfiguration()
dpLayer = SmartNoiseDP(config)
sqlParser = SQLParser(config['privacy']['whitelist'])


class queryHandler(Resource):
    def get(self):

        json_data = request.get_json(force=True)
        query = json_data['query']

        try:
            sqlParser.parse(query)
        except Exception as e:
            return jsonify(e.args)

        try:
            result = dpLayer.executeQuery(query)
        except Exception as e:
            result = e.args

        return jsonify(result)


app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')
app.config.from_object('config')

api = Api(app)
api.add_resource(queryHandler, '/')


'''
curl -d '{"query":"SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married"}' -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/
'''
