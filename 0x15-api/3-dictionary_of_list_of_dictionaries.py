#!/usr/bin/python3
"""Gather data from an API and export to JSON"""
import json
import requests


if __name__ == "__main__":
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todo = requests.get(url + "todos").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({user.get("id"): [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")} for task in todo
                if user.get("id") == task.get("userId")] for user in users},
                  jsonfile)
