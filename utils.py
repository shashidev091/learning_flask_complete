from os import path, listdir, remove
from pandas import DataFrame, read_csv
from typing import Dict

def fetch_data_from_database(APP_ROOT, DATA_FILE) -> DataFrame:
    """This file return csv file that is being treated as database and return type is Dataframe"""
    if len(listdir(path.join(APP_ROOT, 'server_database'))) > 0:
        df = read_csv(DATA_FILE)
        return df
    else:
        return -1


def convert_df_json(df: DataFrame, json):
    todos = []
    todos_json: Dict = json.loads(df.to_json())
    data = [list(item.values()) for item in list(todos_json.values())]
    for todo in zip(*data):
        temp_dict = {}
        for idx, key in enumerate(list(todos_json.keys())):
            temp_dict[key] = todo[idx]
        todos.append(temp_dict)
    return todos
