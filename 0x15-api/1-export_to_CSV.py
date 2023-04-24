#!/usr/bin/python3
'''
A script to export data in CSV format.
'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todos = requests.get(url, verify=False).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            task_writer.writerow([int(uid), user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])
