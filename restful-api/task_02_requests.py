#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url="https://jsonplaceholder.typicode.com/"
    a=requests.get(url)
    print(f"Status Code: 200 {a} ")
    if url
