from opendp.smartnoise import metadata
from opendp.smartnoise.sql import PandasReader, SparkReader, SqlReader, SqlServerReader, PostgresReader
import pandas as pd
from opendp.smartnoise.metadata import CollectionMetadata
import os

DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


def DBReaderFactory(config):
    type = config['type']
    path = config['path']
    metadata = config['metadata']
    if type == 'csv':
        csv_file = pd.read_csv(path)
        meta = CollectionMetadata.from_file(metadata)
        return PandasReader(csv_file, meta)
    elif type == 'sqlreader':
        # ToDo
        pass
