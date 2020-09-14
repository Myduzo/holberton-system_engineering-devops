#!/usr/bin/python3
"""Using what we did in the task #0, extend Python script to export data in the JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
	my_list = []
	d = {}
	d1 = {}
	EMPLOYEE_NAME = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
	req_todo = requests.get('https://jsonplaceholder.typicode.com/todos')
	li = req_todo.json()
	for dec in li:
		for k, v in dec.items():
			if k == "userId" and v == int(argv[1]):
				d = {"task": dec.get("title"), "completed": dec.get("completed"), "username": dec.get("username")}
				my_list.append(d)
			d1 = {argv[1]: my_list}
	with open('{}.json'.format(argv[1]), 'w+') as file:
		file.write(str(d1))
