#!/usr/bin/python3
"""
api requests
"""
import csv
import requests

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print("Title: {}".format(post['title']))

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

    with open("posts.csv", "w", newline='') as file:
        keys = ["id", "title", "body"]
        dict_writer = csv.DictWriter(file, fieldnames=keys)

        dict_writer.writeheader()
        for post in data:
            dict_writer.writerow(post)