from flask import Flask, make_response, jsonify, request, render_template
from random import choice, randint
from string import ascii_letters, punctuation
from device import Printer, BookStore, Book
from pandas import DataFrame, read_csv, concat
from typing import Dict
from os import path, listdir
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
        if len(listdir(path.join(APP_ROOT, 'server_database'))) == 0:
            with open(DATA_FILE, 'w') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(
                    [list(req.keys()), [req.get('task'), req.get('status'), req.get('created_at')]])
        else:
            with open(DATA_FILE, 'r') as csv_reader:
                tasks = [task.split(',')[0] for task in csv_reader.readlines()]
                print(tasks)
                if req.get('task') in tasks:
                    return f"task {req.get('task')}, already exists 🚫"
            with open(DATA_FILE, 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(
                    [req.get('task'), req.get('status'), req.get('created_at')])
    except Exception as e:
        print(e)
    return 'todo added'

@app.patch('/todos')
def update_todo():
    # complete today
    pass
