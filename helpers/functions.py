import pandas as pd
from configs import config
from helpers.file_converter import file_to_df


def get_df(files: list) -> pd.DataFrame:
    df_list = []
    for file in files:
        filename = file.split("/")[-1]
        df = file_to_df(file)
        df['filename'] = filename
        df_list.append(df)
        config.logger.info(f'{filename} file converted')
    return pd.concat(df_list).reset_index()


def df_processing(total_df: pd.DataFrame) -> dict:
    config.logger.info(f'DataFrame processing...')
    target_person_df = total_df.loc[total_df['Full_name'] == 'Jason Bourne']
    target_person_series = target_person_df.loc[0].squeeze()
    valid_persons_df = total_df[(total_df['Passport_number'] == target_person_series['Passport_number']) | (total_df['Flight_ticket'] == target_person_series['Flight_ticket'])]
    return valid_persons_df.to_dict('records')
