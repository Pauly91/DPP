
from app.DPLayer.DPBase import DPBase
from app.DPLayer.DPReaderFactory import DBReaderFactory
from opendp.smartnoise.metadata import CollectionMetadata
from opendp.smartnoise.sql import PrivateReader


class SmartNoiseDP(DPBase):
    def __init__(self, configuration):
        self.reader = DBReaderFactory(configuration)
        self.meta = CollectionMetadata.from_file(configuration['metadata'])
        # epsilon is 0.1, delta is 10E-16
        self.privacyParameter = {
            "epsilon": 0.01,
            "delta": 10E-16
        }

    def setPrivacyParameter(self, privacyParameter):
        self.privacyParameter['epsilon'] = privacyParameter['epsilon']
        self.privacyParameter['delta'] = privacyParameter['delta']

    def executeQuery(self, query):
        private_reader = PrivateReader(
            self.reader, self.meta, self.privacyParameter['epsilon'], self.privacyParameter['delta'])
        return private_reader.execute(query)
