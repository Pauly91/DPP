from opendp.smartnoise import metadata
from opendp.smartnoise.sql import PandasReader, SparkReader, SqlReader, SqlServerReader, PostgresReader
from opendp.smartnoise.metadata import CollectionMetadata

import os
import pandas as pd

DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')


def SNReaderFactory(config):
    type = config['type']
    path = config['dbpath']
    metadata = config['metadata']
    if type == 'csv':
        csv_file = pd.read_csv(path)
        meta = CollectionMetadata.from_file(metadata)
        return PandasReader(csv_file, meta)
    elif type == 'sql':
        pass
    elif type == 'spark':

        pass
    elif type == 'sqlserver':
        pass
    elif type == 'postgres':
        pass
