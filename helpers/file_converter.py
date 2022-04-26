import pandas as pd
from configs import config


def file_to_df(file_path: str) -> pd.DataFrame:
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)

    file_format = file_path.split('.')[-1]
    convert_func = config.FILE_FORMATS_DICT[file_format]
    return eval(convert_func)(file_path)


def json_converter(path: str) -> pd.DataFrame:
    return pd.read_json(path)
