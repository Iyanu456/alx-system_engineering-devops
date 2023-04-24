#!/usr/bin/python3
'''
Python script that returns information using a REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            j_req = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            all_tasks = len(j_req)
            completed_tasks = []
            for t in j_req:
                if t.get("completed") is True:
                    completed_tasks.append(t)
            count = len(completed_tasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, all_tasks))
            for title in completed_tasks:
                print("\t {}".format(title.get("title")))
