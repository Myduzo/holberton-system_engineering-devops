#!/usr/bin/python3
"""script that returns information about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    req_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))
    name = req_name.json().get("name")

    req_todo = requests.get("http://jsonplaceholder.typicode.com/todos")
    todo = req_todo.json()

    tasks_done = []
    totaltasks = 0
    for task in todo:
        if task.get("userId") == int(userId):
            totaltasks += 1
            if task.get("completed"):
                tasks_done.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(tasks_done), totaltasks))

    for element in tasks_done:
        print("\t {}".format(element))
