#!/usr/bin/python3
"""
Using what we did in the task #0, extend Python script
to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    userId = argv[1]
    req_name = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))
    name = req_name.json().get("username")

    req_todo = requests.get("http://jsonplaceholder.typicode.com" +
                            "/todos".format(userId))
    todo = req_todo.json()

    with open('{}.csv'.format(userId), 'w') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([userId, name, str(task.get('completed')),
                            task.get('title')])
