#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""


import requests
from sys import argv


def main():
    """ returns info about TODO list """
    total = 0
    complete = 0
    user = "https://jsonplaceholder.typicode.com/users/"
    t_url = "https://jsonplaceholder.typicode.com/todos?userId="
    user_req = requests.get('{}{}'.format(user, argv[1])).json()
    task_req = requests.get('{}{}'.format(t_url, argv[1])).json()

    for task in task_req:
        if task['completed'] is True:
            complete += 1
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(user['name'],
          complete, total))
    for task in task_req:
        if task['completed'] is True:
            print("\t {}".format(task['title']))

if __name__ == "__main__":
    main()
