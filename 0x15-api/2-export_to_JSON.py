#!/usr/bin/python3
"""
Module Name: 2-export_to_JSON.py
Description: Python script that exports employee
TODO list progress to a JSON file.
"""


import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Make a GET request to the API
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    tasks_url = f"{base_url}/todos?userId={employee_id}"
    try:
        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)
        user_response.raise_for_status()
        tasks_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Extract relevant data
    user = user_response.json()
    tasks = tasks_response.json()

    # Prepare data for JSON export
    data = {
        str(employee_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": user["username"]
            }
            for task in tasks
        ]
    }

    # Export data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(data, file)

    print(f"Data exported to {filename} successfully.")
