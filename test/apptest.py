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

    def test_app_result(self):

        response = self.app.get('/',
                                data=json.dumps(dict(
                                    query='SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married')),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        jsonData = response.get_json()
        self.assertEqual(['married', 'income', 'n'], jsonData[0])

    def test_app_exception_whitelist(self):

        response = self.app.get('/',
                                data=json.dumps(dict(
                                    query='SELECT married, Hello(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married')),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        jsonData = response.get_json()
        self.assertEqual(
            "Expression 'HELLO' not found in the allowed list: (,ABS,ACOS,ASIN,ATAN,AVG,CASE,CEILING,CHOOSE,COS,COUNT,DEGREES,DENSE_RANK,EXP,FALSE,FLOOR,IIF,LOG,LOG10,MAX,MIN,NEWID,NULL,PERCENTILE_CONT,PERCENTILE_DISC,PI,POWER,RAND,RANDOM,RANK,ROUND,ROW_NUMBER,SIGN,SIN,SQRT,SQUARE,STD,STDDEV,SUM,TAN,TRUE,VAR,VARIANCE,-,*,STRING,INTEGER_VALUE,DECIMAL_VALUE,QN2,IDENT", jsonData[0])

    def test_app_exception_invalidQuery(self):

        response = self.app.get('/',
                                data=json.dumps(dict(
                                    query='SELECT married, sin(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married')),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        jsonData = response.get_json()
        self.assertEqual(
            'Error in sql query: Select column not a supported type: SIN ( PUMS.PUMS.income )', jsonData)
