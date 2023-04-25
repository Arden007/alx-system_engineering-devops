#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = sys.argv[1]
    employee_url = url + user_id
    res = requests.get(employee_url)
    username = res.json().get('username')

    todo_url = employee_url + "/todos"
    res = requests.get(todo_url)
    tasks = res.json()

    with open('{}.csv'.format(user_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(user_id, username, task.get('completed'), task.get('title')))
