#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
from sys import argv


if __name__ == "__main__":

    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))

    EMPLOYEE_NAME = r.json().get('name')

    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(argv[1]))

for task in requests.get(r).json():
        if user["id"] == task["userId"]:
            total_tasks += 1
            if task["completed"] is True:
                task_list.append(task["title"])
                completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], completed_tasks, total_tasks))
    for title in task_list:
        print("\t {}".format(title))
