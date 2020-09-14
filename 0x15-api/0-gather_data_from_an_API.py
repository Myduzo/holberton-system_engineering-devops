#!/usr/bin/python3
"""script that returns information about his/her TODO list progress."""

import requests
from sys import argv


if __name__ == "__main__":
	EMPLOYEE_NAME = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json().get('name')
	req_todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()
	my_list = []
	TOTAL_NUMBER_OF_TASKS = 0
	for task in req_todo:
		if task.get('userId') == int(argv[1]):
			TOTAL_NUMBER_OF_TASKS += 1
			if str(task.get('completed')) == 'True':
				my_list.append(task.get('title'))
	print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME, len(my_list), TOTAL_NUMBER_OF_TASKS))
	for index in my_list:
		print('\t {}'.format(index))
