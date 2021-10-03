
from app.DPLayer.DPBase import DPBase
from app.DPLayer.SmartNoise.smartNoiseReaderFactory import SNReaderFactory

from opendp.smartnoise.metadata import CollectionMetadata
from opendp.smartnoise.sql import PrivateReader


class SmartNoiseDP(DPBase):
    def __init__(self, configuration):
        reader = SNReaderFactory(configuration)
        meta = CollectionMetadata.from_file(configuration['metadata'])
        privacyParameter = configuration['privacy']
        self.private_reader = PrivateReader(
            reader, meta, privacyParameter['epsilon'], privacyParameter['delta'])

    def executeQuery(self, query):

        try:
            result = self.private_reader.execute(query)
        except ValueError as err:
            result = "Error in sql query: " + str(err)

        return result
