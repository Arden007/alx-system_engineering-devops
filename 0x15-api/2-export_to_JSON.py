#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import json
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

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in tasks]}, jsonfile)
