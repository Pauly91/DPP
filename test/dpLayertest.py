
from app.DPLayer.DPReaderFactory import DBReaderFactory
from app.DPLayer.smartNoiseDP import SmartNoiseDP

import unittest
import os

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


class dpLayerTest(unittest.TestCase):

    def test_readerFactory(self):
        config = {
            "type": "csv",
            "path":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        reader = DBReaderFactory(config)
        self.assertEqual(reader.engine, 'Pandas')

    def test_smartNoiseDPClass(self):
        config = {
            "type": "csv",
            "path":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        smDP = SmartNoiseDP(config)
        self.assertEqual(smDP.reader.engine, 'Pandas')

    def test_smartNoiseQuery(self):
        config = {
            "type": "csv",
            "path":  os.path.join(TESTDATA_DIRECTORY, 'PUMS.csv'),
            "metadata": os.path.join(TESTDATA_DIRECTORY, 'PUMS_row.yaml')
        }
        smDP = SmartNoiseDP(config)
        query = 'SELECT married, AVG(income) AS income, COUNT(*) AS n FROM PUMS.PUMS GROUP BY married'
        result = smDP.executeQuery(query)
        self.assertEqual(smDP.reader.engine, 'Pandas')


if __name__ == '__main__':
    unittest.main()
