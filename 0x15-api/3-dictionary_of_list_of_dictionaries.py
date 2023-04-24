#!/usr/bin/python3
'''
A script to export data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    us = requests.get(url, verify=False).json()
    un_doc = {}
    u_doc = {}
    for user in us:
        uid = user.get("id")
        u_doc[uid] = []
        un_doc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url, verify=False).json()
    [u_doc.get(todo.get("userId")).append({"task": todo.get("title"),
                                       "completed": todo.get("completed"),
                                       "username": un_doc.get(
                                               todo.get("userId"))})
     for todo in todos]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(u_doc, jsf)
