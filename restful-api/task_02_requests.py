#!/usr/bin/python3


import requests
import csv


def fetch_and_print_posts():
     url = "https://jsonplaceholder.typicode.com/posts"
     response = requests.get(url)

     print(f"Status Code: {response.status_code}")

     if response.status_code == 200:
         posts = response.json()
         for post in posts:
             print(post["title"])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        list_posts = []
        for post in posts:
            list_posts.append({
                "id": post["id"],
                 "title": post["title"],
                 "body": post["body"]
            })
        with open('posts.csv', 'w') as csvfile:
             fieldnames = ['id', 'title', 'body']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

             writer.writeheader()
             writer.writerows(list_posts)
