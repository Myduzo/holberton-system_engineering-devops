#!/usr/bin/python3
"""script that returns information about his/her TODO list progress."""

import requests
from sys import argv


if __name__ == "__main__":
    if argv[1].isdigit():

        req_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1]))
        name = req_name.json().get("name")

        req_todo = requests.get("http://jsonplaceholder.typicode.com/" +
                                "users/{}/todos".format(argv[1]))
        todo = req_todo.json()

        tasks_done = []
        for task in todo:
            if task.get("completed"):
                tasks_done.append(task.get("title"))
        print("Employee {} is done with tasks({}/{}):"
              .format(name, len(tasks_done), len(todo)))

        for element in tasks_done:
            print("\t {}".format(element))
