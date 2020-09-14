#!/usr/bin/python3
"""Using what we did in the task #0, extend Python script to export data in the CSV format."""

import requests
from sys import argv


if __name__ == "__main__":
	EMPLOYEE_NAME = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json().get('name')
	req_todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

	with open('{}.csv'.format(argv[1]), 'w+') as file:
			for task in req_todo:
				if task.get('userId') == int(argv[1]):
					file.write('"{}","{}","{}","{}"\n'.format(task.get('userId'), EMPLOYEE_NAME, task.get('completed'), task.get('title')))
