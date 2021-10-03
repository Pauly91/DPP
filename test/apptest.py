import unittest
from app import app
import json


class appTest(unittest.TestCase):
    # executed prior to each test

    def setUp(self):

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_appPost(self):

        response = self.app.post('/',
                                 data=json.dumps(dict(
                                     query='SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married')),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        jsonData = response.get_json()
        self.assertEqual(['married', 'income', 'n'], jsonData[0])
