import logging
from operator import or_
from functools import reduce
from difflib import SequenceMatcher

import numpy as np
import pandas as pd
from configs import config


logger = logging.getLogger('file processor')


class FileProcessor:
    def __init__(self, files):
        self.files = files
        self.df_list = []
        self.total_df = pd.DataFrame()

    def files_to_df(self):
        for file in self.files:
            file_name = file.split('/')[-1]
            extension = file.split('.')[-1]
            df = config.FILE_READERS[extension](file).to_dataframe()
            df['file_name'] = file_name
            self.df_list.append(df)
            logger.info(f'{file_name} file converted')
        self.total_df = pd.concat(self.df_list).reset_index()

    def get_similarity(self, first_value, second_value):
        return SequenceMatcher(None, str(first_value), str(second_value)).ratio()

    def search_by_parameters(self, target_person_series: pd.Series) -> pd.DataFrame:
        similarity_func = np.vectorize(self.get_similarity)
        query = [similarity_func(self.total_df[param], target_person_series[param]) >= config.MATCHING_VALUE_THRESHOLD
                 for param in config.SEARCH_BY_PARAMETERS]
        return self.total_df[reduce(or_, query)]

    def search_identity(self) -> pd.DataFrame:
        identity = [self.total_df.loc[self.total_df[k] == v] for k, v in config.SEARCH_IDENTITY.items()]
        return identity[0]

    def get_target_persons(self) -> dict:
        target_person_df = self.search_identity()
        target_person_series = target_person_df.loc[0].squeeze()
        # print(target_person_series)
        valid_persons_df = self.search_by_parameters(target_person_series=target_person_series)
        return valid_persons_df.to_dict('records')

    def df_processing(self) -> dict:
        logger.info(f'DataFrame processing...')
        self.files_to_df()
        return self.get_target_persons()
