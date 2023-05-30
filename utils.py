from os import path, listdir, remove
from pandas import DataFrame, read_csv
from typing import Dict
from enum import Enum
from datetime import datetime, timedelta

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



# class Moment(Enum):
#     NOW = now
    
#     TOMORROW = tomorrow

#     YESTERDAY = yesterday


def task_moment(moment):
    now = f'({datetime.now().strftime("%d/%m/%Y %H:%M:%S")})'
    tomorrow = f'({datetime.now() + timedelta(1)})'
    yesterday = f'({datetime.now() - timedelta(1)})'
    if moment == 'now' or moment == 'today':
        return now
    if moment == 'tomorrow':
        return tomorrow
    if moment == 'yesterday':
        return yesterday
    
    try:
        parse_moment = int(moment)
        return f'({datetime.now() + timedelta(parse_moment)})'
    except Exception as e:
        return "Invalid input"