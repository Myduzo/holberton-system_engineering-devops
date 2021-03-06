#!/usr/bin/python3
"""
Using what we did in the task #0, extend Python script
to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    req_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(argv[1]))
    name = req_name.json().get("username")

    req_todo = requests.get("http://jsonplaceholder.typicode.com/" +
                            "users/{}/todos".format(argv[1]))
    todo = req_todo.json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([argv[1], name, str(task.get('completed')),
                            task.get('title')])
