from flask import Flask, make_response, jsonify, request, render_template
from random import choice, randint
from string import ascii_letters, punctuation
from device import Printer, BookStore, Book
from pandas import DataFrame, read_csv, concat
from typing import Dict
from os import path, listdir, remove
import csv
import json


app = Flask(__name__)
APP_ROOT = app.root_path
DATA_FILE = path.join(APP_ROOT, 'server_database/datastorage.csv')


# get todos
@app.get('/todos')
def get_todos():
    df = read_csv(DATA_FILE)
    todos_json_str = df.to_json()
    todos_json: Dict = json.loads(todos_json_str)

    todos = []

    data = [list(item.values()) for item in list(todos_json.values())]
    for todo in zip(*data):
        temp_dict = {}
        for idx, key in enumerate(list(todos_json.keys())):
            temp_dict[key] = todo[idx]
        todos.append(temp_dict)
    return todos


@app.put('/todos')
def add_todo():
    req: Dict = request.get_json()
    try:
        if len(listdir(path.join(APP_ROOT, 'server_database'))) != 0:
            with open(DATA_FILE, 'r') as csv_reader:
                tasks = [task.split(',')[0] for task in csv_reader.readlines()]
                if req.get('task') in tasks:
                    return f"task {req.get('task')}, already exists 🚫"
        if len(listdir(path.join(APP_ROOT, 'server_database'))) == 0:
            with open(DATA_FILE, 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                header = list(req.keys())
                header.insert(0, 'id')
                csv_writer.writerow(header)
                csv_writer.writerow(
                    [1, req.get('task'), req.get('status'), req.get('created_at')])
        else:
            with open(DATA_FILE, 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(
                    [len(fetch_data_from_database().index) + 1, req.get('task'), req.get('status'), req.get('created_at')])
    except Exception as e:
        return str(e)
    return 'todo added'


@app.patch('/todos/<int:task_id>')
def update_todo(task_id):
    # complete today
    df = fetch_data_from_database()
    element = df[df['id'] == task_id]
    # print(df.loc[task_id - 1])
    element["task"] = "This world need a great developer who can unleash the power of clustering in pc."
    print(element['task'])
    if element.empty:
        return f"task_id = {task_id} not found, enter valid task id.🦥"
    else:
        todos = get_todos()
        remove(DATA_FILE)
        with open(DATA_FILE, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)

    return element.to_json()


def fetch_data_from_database() -> DataFrame:
    """This file return csv file that is being treated as database and return type is Dataframe"""
    if len(listdir(path.join(APP_ROOT, 'server_database'))) > 0:
        df = read_csv(DATA_FILE)
        return df
    else:
        return -1


def convert_df_json(df: DataFrame):
    todos = []
    todos_json: Dict = json.loads(df.to_json())
    data = [list(item.values()) for item in list(todos_json.values())]
    for todo in zip(*data):
        temp_dict = {}
        for idx, key in enumerate(list(todos_json.keys())):
            temp_dict[key] = todo[idx]
        todos.append(temp_dict)
    return todos
