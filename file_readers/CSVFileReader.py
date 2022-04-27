import logging
import pandas as pd

from file_readers.base import AbstractFileReader


logger = logging.getLogger('CSV reader')


class CSVFileReader(AbstractFileReader):
    def to_dataframe(self):
        logger.info(f'{self.file} file converting...')
        return pd.read_csv(self.file)
