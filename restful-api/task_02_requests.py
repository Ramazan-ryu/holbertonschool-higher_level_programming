#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    a=requests.get(url)
    print(f"Status Code: 200 {a.status_code}")
    if a.status_code==200:
        for j in a.json():
            print(j)

def fetch_and_save_posts():
    url="https://jsonplaceholder.typicode.com/posts"
    a=requests.get(url)
    posts=[{"id": post["id"],"title":post["title"],"body":post["body"]} for post in a.json()]
    with open('posts.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'title', 'body'])
        for post in posts:
            writer.writerow([post['id'], post['title'], post['body']])
