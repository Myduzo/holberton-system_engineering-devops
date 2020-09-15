#!/usr/bin/python3
"""
Using what we did in the task #0, extend Python script
to export data in the CSV format.
"""

import csv
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

        with open('{}.csv'.format(argv[1]), 'w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL, lineterminator='\n')
            for task in todo:
                if task.get('userId') == int(argv[1]):
                    writer.writerow([argv[1], name, str(task.get('completed')),
                                    task.get('title')])
