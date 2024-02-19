#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    # Make a GET request to retrieve all users
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    try:
        users_response = requests.get(users_url)
        users_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Extract the users data
    users = users_response.json()

    # Prepare data for JSON export
    data = {}
    for user in users:
        user_id = str(user["id"])
        username = user["username"]

        # Make a GET request to retrieve the tasks for each user
        tasks_url = f"{base_url}/todos?userId={user_id}"
        try:
            tasks_response = requests.get(tasks_url)
            tasks_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            sys.exit(1)

        # Extract the tasks data
        tasks = tasks_response.json()

        # Add the tasks data to the main data dictionary
        data[user_id] = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in tasks
        ]

    # Export data to JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file)

    print(f"Data exported to {filename} successfully.")
