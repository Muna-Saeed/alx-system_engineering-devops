#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # Make a GET request to retrieve all tasks
    base_url = "https://jsonplaceholder.typicode.com"
    tasks_url = f"{base_url}/todos"
    try:
        tasks_response = requests.get(tasks_url)
        tasks_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Extract the tasks data
    tasks = tasks_response.json()

    # Prepare data for JSON export
    data = {}
    for task in tasks:
        user_id = str(task["userId"])
        task_data = {
            "username": None,
            "task": task["title"],
            "completed": task["completed"]
        }

        if user_id not in data:
            data[user_id] = []

        data[user_id].append(task_data)

    # Make a GET request to retrieve all users
    users_url = f"{base_url}/users"
    try:
        users_response = requests.get(users_url)
        users_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Extract the users data
    users = users_response.json()

    # Update the usernames in the data dictionary
    for user in users:
        user_id = str(user["id"])
        if user_id in data:
            for task_data in data[user_id]:
                task_data["username"] = user["username"]

    # Export data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file)

    print(f"Data exported to {filename} successfully.")
