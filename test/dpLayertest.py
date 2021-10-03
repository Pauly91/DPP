
from warnings import catch_warnings
from app.DPLayer.smartNoiseReaderFactory import SNReaderFactory
from app.DPLayer.smartNoiseDP import SmartNoiseDP
from opendp.smartnoise.sql.parse import QueryParser
import pandas as pd
from opendp.smartnoise.sql import PandasReader, PrivateReader
from opendp.smartnoise.metadata import CollectionMetadata
from opendp.smartnoise.sql.parse import QueryParser

import unittest
import os
import sqlparse

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


class dpLayerTest(unittest.TestCase):

    def test_readerFactory(self):
        config = {
            "type": "csv",
            "dbpath":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        reader = SNReaderFactory(config)
        self.assertEqual(reader.engine, 'Pandas')

    def test_smartNoiseDPClass(self):
        config = {
            "type": "csv",
            "dbpath":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        smDP = SmartNoiseDP(config)
        self.assertEqual(smDP.reader.engine, 'Pandas')

    def test_smartNoiseQuery(self):
        config = {
            "type": "csv",
            "dbpath":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        smDP = SmartNoiseDP(config)
        query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        result = smDP.executeQuery(query)
        self.assertEqual(len(result), 3)

    def test_smartNoiseQuery_1(self):
        config = {
            "type": "csv",
            "dbpath":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        smDP = SmartNoiseDP(config)
        query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        try:
            result = smDP.executeQuery(query)
        except ValueError as err:
            print(err)


if __name__ == '__main__':
    unittest.main()
