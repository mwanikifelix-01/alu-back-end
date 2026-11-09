#!/usr/bin/python3
"""
Uses the JSONPlaceholder REST API to export all tasks owned by
a given employee ID to a CSV file named USER_ID.csv.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
