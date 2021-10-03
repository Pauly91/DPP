

from app.DPLayer.SmartNoise.smartNoiseReaderFactory import SNReaderFactory
from app.DPLayer.SmartNoise.smartNoiseDP import SmartNoiseDP

from opendp.smartnoise.sql.parse import QueryParser
from opendp.smartnoise.sql import PandasReader, PrivateReader
from opendp.smartnoise.metadata import CollectionMetadata
from opendp.smartnoise.sql.parse import QueryParser

import unittest
import os


TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')
config = {
    "type": "csv",
    "dbpath":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
    "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml'),
    "privacy":
    {
        "epsilon": 1,
        "delta": 10E-16,
        "whitelist": "(,ABS,ACOS,ASIN,ATAN,AVG,CASE,CEILING,CHOOSE,COS,COUNT,DEGREES,DENSE_RANK,EXP,FALSE,FLOOR,IIF,LOG,LOG10,MAX,MIN,NEWID,NULL,PERCENTILE_CONT,PERCENTILE_DISC,PI,POWER,RAND,RANDOM,RANK,ROUND,ROW_NUMBER,SIGN,SIN,SQRT,SQUARE,STD,STDDEV,SUM,TAN,TRUE,VAR,VARIANCE,-,*,STRING,INTEGER_VALUE,DECIMAL_VALUE,QN2,IDENT"
    }
}


class dpLayerTest(unittest.TestCase):

    def test_readerFactory(self):

        reader = SNReaderFactory(config)
        self.assertEqual(reader.engine, 'Pandas')

    def test_smartNoiseDPClass(self):

        smDP = SmartNoiseDP(config)
        self.assertEqual(smDP.private_reader.engine, 'Pandas')

    def test_smartNoiseQuery(self):

        smDP = SmartNoiseDP(config)
        query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        result = smDP.executeQuery(query)
        self.assertEqual(len(result), 3)

    def test_smartNoiseQuery_1(self):

        smDP = SmartNoiseDP(config)
        query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        try:
            result = smDP.executeQuery(query)
        except ValueError as err:
            print(err)


if __name__ == '__main__':
    unittest.main()
