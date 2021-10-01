
from flask_restful import Resource, Api
from flask import request, jsonify
from app.DPLayer.smartNoiseDP import SmartNoiseDP
from app.configuration.connector import getConfiguration


class queryHandler(Resource):
    def __init__(self):
        appConfig = getConfiguration('app')
        privacyConfig = getConfiguration('privacy')
        self.dpLayer = SmartNoiseDP(appConfig)
        self.dpLayer.setPrivacyParameter(privacyConfig)

    def get(self):
        return {"hello": "Hello Worldsadas"}

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        query = json_data['query']
        return jsonify(self.dpLayer.executeQuery(query))


'''
tuts: https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework
curl -d '{"query":"SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/
'''
