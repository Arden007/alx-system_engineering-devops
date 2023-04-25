#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    user_id = sys.argv[1]
    employee_url = url + user_id
    res = requests.get(employee_url)
    Name = res.json().get('name')

    todo_url = employee_url + "/todos"
    res = requests.get(todo_url)
    tasks = res.json()
    completed = 0
    task_List = []

    for task in tasks:
        if task.get('completed'):
            task_List.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(Name, completed, len(tasks)))

    for task in task_List:
        print("\t {}".format(task.get('title')))