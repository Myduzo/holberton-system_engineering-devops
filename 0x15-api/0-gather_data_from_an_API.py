#!/usr/bin/python3
"""script that returns information about his/her TODO list progress."""

import requests
from sys import argv


if __name__ == "__main__":
    req_todo = requests.get("http://jsonplaceholder.typicode.com/" +
                            "users/{}/todos".format(argv[1]))
    todo = req_todo.json()

    req_name = requests.get("http://jsonplaceholder.typicode.com/" +
                            "users/{}".format(argv[1]))
    name = req_name.json()["name"]

    tasks_done = []
    for task in todo:
        if task["completed"] is True:
            tasks_done.append(task["title"])
    print("Employee {} is done with ".format(name) +
          "tasks({}/{}):".format(len(tasks_done), len(todo)))

    for index in tasks_done:
        print("\t {}".format(index))
