#!/usr/bin/python3
"""
Uses the JSONPlaceholder REST API to export all tasks owned by
a given employee ID to a JSON file named USER_ID.json.
"""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()
    username = user.get("username")

    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: tasks}, f)