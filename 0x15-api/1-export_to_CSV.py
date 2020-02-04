#!/usr/bin/python3
"""
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
import requests
import sys


if __name__ == "__main__":
    new_dict = {}
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(argv[1])).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    with open("{}.csv".format(argv[1]), "w") as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in requests.get(url).json():
            if user["id"] == task["userId"]:
                for k, v in task.items():
                    if k != "id":
                        new_dict[k] = str(v)
                new_dict["username"] = user["username"]
                writer.writerow(new_dict)
