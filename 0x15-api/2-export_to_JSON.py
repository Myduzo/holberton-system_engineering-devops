#!/usr/bin/python3
"""Using what we did in the task #0
extend Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    req_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    name = req_name.json().get("username")

    req_todo = requests.get("http://jsonplaceholder.typicode.com/" +
                            "users/{}/todos".format(argv[1]))
    todo = req_todo.json()
    
    with open("{}.json".format(argv[1]), "w") as jsonfile:
        out = [{
                "task":         task.get('title'),
                "completed":    task.get('completed'),
                "username":     name
               } for task in todo]

        json.dump({"{}".format(argv[1]): out}, jsonfile)
