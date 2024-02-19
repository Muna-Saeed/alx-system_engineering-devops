#!/usr/bin/python3
"""
Module Name: 0-gather_data_from_an_API.py
Description: Python script that, using a REST API, returns
information about an employee's TODO list progress.
Author: Your Name
"""


import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Make a GET request to the API
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_response.raise_for_status()
        todos_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Extract relevant data
    user = user_response.json()
    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    # Display progress
    print(
        f"Employee {user['name']} is done with tasks({completed_tasks}/"
        f"{total_tasks}):"
    )
    for todo in todos:
        if todo["completed"]:
            print(f"\t{todo['title']}")
