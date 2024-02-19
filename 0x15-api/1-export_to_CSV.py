#!/usr/bin/python3
"""
Module Name: 1-export_to_CSV.py
Description: Python script that exports
employee TODO list progress to a CSV file.
Author: Your Name
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"
    .format(employee_id)
    tasks_url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    .format(employee_id)

    response_user = requests.get(user_url)
    response_tasks = requests.get(tasks_url)

    if response_user.status_code != 200:
        print("User not found")
        exit(1)

    if response_tasks.status_code != 200:
        print("Tasks not found")
        exit(1)

    user = response_user.json()
    tasks = response_tasks.json()

    csv_filename = "{}.csv".format(employee_id)

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([
                user['id'],
                user['username'],
                str(task['completed']),
                task['title']
            ])

    print("Data exported to", csv_filename)
