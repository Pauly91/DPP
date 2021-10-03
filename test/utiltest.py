from app.utils.configParser import Parser
import unittest
import os
from app.utils.sqlParser import SQLParser

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


class MyException(Exception):
    def __str__(self) -> str:
        return repr("Expression 'TEST' not found in the allowed list: sum,call")


class utilitiesTest(unittest.TestCase):
    def test_parser(self):

        TESTDATA_FILENAME = os.path.join(
            TESTDATA_DIRECTORY, 'testConfig.json')
        data = Parser.parse(TESTDATA_FILENAME)
        self.assertTrue(data['dataBaseType'], 'CSV')
        self.assertTrue(data['dataBasePath'], 'database')

    def test_sqlParser_basic(self):
        query = 'SELECT married, test(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        sp = SQLParser("sum,call")
        try:
            sp.parse(query)
        except Exception as err:
            self.assertEqual(
                err.args[0], "Expression 'TEST' not found in the allowed list: sum,call")

    def test_sqlParser_advanced(self):
        query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        sp = SQLParser("(,ABS,ACOS,ASIN,ATAN,AVG,CASE,CEILING,CHOOSE,COS,COUNT,DEGREES,DENSE_RANK,EXP,FALSE,FLOOR,IIF,LOG,LOG10,MAX,MIN,NEWID,NULL,PERCENTILE_CONT,PERCENTILE_DISC,PI,POWER,RAND,RANDOM,RANK,ROUND,ROW_NUMBER,SIGN,SIN,SQRT,SQUARE,STD,STDDEV,SUM,TAN,TRUE,VAR,VARIANCE,-,*,STRING,INTEGER_VALUE,DECIMAL_VALUE,QN2,IDENT")
        try:
            sp.parse(query)
        except Exception:
            self.fail("Should not raise")


if __name__ == '__main__':
    unittest.main()
