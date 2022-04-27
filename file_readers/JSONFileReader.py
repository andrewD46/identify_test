import logging
import pandas as pd

from file_readers.base import AbstractFileReader


logger = logging.getLogger('JSON reader')


class JSONFileReader(AbstractFileReader):
    def to_dataframe(self):
        logger.info(f'{self.file} file converting...')
        return pd.read_json(self.file)
