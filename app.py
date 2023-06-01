from flask import Flask, make_response, jsonify, request, render_template
from random import choice, randint
from string import ascii_letters, punctuation
from device import Printer, BookStore, Book
from pandas import DataFrame, read_csv, concat
from typing import Dict
from os import path, listdir, remove
import csv
import json
from utils import fetch_data_from_database, convert_df_json, task_moment
from requests import get

app = Flask(__name__)
APP_ROOT = app.root_path
DATA_FILE = path.join(APP_ROOT, 'server_database/datastorage.csv')
ANIME_FILE = path.join(APP_ROOT, 'server_database/anime_storage.json')


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
                    [1, req.get('task'), req.get('status'), task_moment(req.get('created_at').lower())])
        else:
            with open(DATA_FILE, 'a') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(
                    [len(fetch_data_from_database(APP_ROOT, DATA_FILE).index) + 1, req.get('task'), req.get('status'), task_moment(req.get('created_at').lower())])
    except Exception as e:
        return str(e)
    return 'todo added'


@app.patch('/todos/<int:task_id>')
def update_todo(task_id):
    df = fetch_data_from_database(APP_ROOT, DATA_FILE)
    element = df[df['id'] == task_id]
    element["task"] = "This world need a great developer who can unleash the power of clustering in pc."
    print(element['task'])
    if element.empty:
        return f"task_id = {task_id} not found, enter valid task id.🦥"
    else:
        df.to_csv(DATA_FILE, index=False)
        print("")

    return element.to_json()


# Anime management Api's

@app.get("/anime")
def get_animes():
    # get all animes
    # keys = ('title', 'duration', 'status', 'times_watch', 'started_at',
    #         'completed_at', 'progress_episode', 'genre', 'total_episodes')
    anime = [
        {
            'title': 'Death Note',
            'duration': '23m',
            'status': 'Finished Airing',
            'times_watch': 3,
            'started_at': 'Sat Jun 18 2015 18:23:08 GMT+0530',
            'completed_at': 'Sat Jun 20 2015 18:23:08 GMT+0530',
            'progress_eposode': 'Completed',
            'genre': ('Mystery', 'Shounen', 'Supernatural', 'Police', 'Psychological', 'Thriller'),
            'total_episodes': 37
        }
    ]

    df = DataFrame(anime)
    df.to_json(ANIME_FILE)

    return anime


@app.get('/save_anime_data')
def download_any_thing():
    url = request.get_json()['url']
    url_new = f"https://myanimelist.net/animelist/Akarin/load.json?offset=0&status=7"
    # data = get(url)

    # json_data = json.loads(data.content)
    # json_dumps = json.dumps(data.content.decode("utf-8"))
    # with open(path.join(APP_ROOT, 'server_database/anime_data2.json'), 'w', encoding="utf-8") as json_file:
    #     json_file.write(json_dumps)
    # df.to_json(path.join(APP_ROOT, 'server_database/anime_data.json'))
    main_list = {}
    flag = True
    item = 0
    while flag:
        data = get(f"https://myanimelist.net/animelist/Akarin/load.json?offset={item}&status=7")
        json_loads = json.loads(data.content.decode('utf-8'))
        if len(json_loads) <= 0:
            flag = False
            break
        print(len(json_loads), item)
        main_list[str(item)] = json_loads
        item += 300
        
    
    with open(path.join(APP_ROOT, 'server_database/anime_data3.json'), 'w', encoding="utf-8") as json_file:
        json_file.write(json.dumps(main_list))

    return main_list