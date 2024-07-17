#!/usr/bin/python3
"""
api requests
"""
import csv
import requests

def fetch_and_print_posts():
    """
    fetches all posts from JSONPlaceholder and prints their titles
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them into a CSV file
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": post["id"], "title": post["title"], 
                 "body": post["body"]} for post in posts]

        with open("posts.csv", "w", newline='') as file:
            keys = ["id", "title", "body"]
            dict = csv.DictWriter(file, fieldnames=keys)

            dict.writeheader()
            for post in data:
                dict.writerow(post)
