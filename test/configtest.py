from app.utils.configParser import Parser
import unittest
import os

TESTDATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


class configurationParserTest(unittest.TestCase):
    def test_parser(self):

        TESTDATA_FILENAME = os.path.join(
            TESTDATA_DIRECTORY, 'testConfig.json')
        data = Parser.parse(TESTDATA_FILENAME)
        self.assertTrue(data['dataBaseType'], 'CSV')
        self.assertTrue(data['dataBasePath'], 'database')


if __name__ == '__main__':
    unittest.main()
