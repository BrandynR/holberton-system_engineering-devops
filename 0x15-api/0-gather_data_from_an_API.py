#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users", params={"id": sys.argv[1]})
    for names in user.json():
        user_id = names.get('id')
        todo = requests.get(url + "/todos", params={"userId": user_id})
        task_complete = 0
        tasks_array = []
        for tasks in todo.json():
            if tasks.get('completed') is True:
                task_complete += 1
                tasks_array.append(tasks.get('title'))
        print("Employee {:s} is done with tasks({:d}/{:d}):\n\t {}".
              format(names.get('name'), task_complete,
                     len(todo.json()), "\n\t ".join(tasks_array)))
