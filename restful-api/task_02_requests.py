#!/usr/bin/python3

import requests


def fetch_and_print_posts():
     url = "https://intranet.hbtn.io/rltoken/Ut3d3Tzd0l_sH0evg3GiMg"
     response = requests.get(url)

     print(f"Status Code: {response.status_code}")

     if response.status_code == 200:
         posts = response.json()
         for post in posts:
             print(post["title"])
def fetch_and_save_posts():
