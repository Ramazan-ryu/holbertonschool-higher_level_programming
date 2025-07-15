#!/usr/bin/python3


'''
Background:
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The requests library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.

Objective:
At the end of this exercise, students should be able to:

Utilize the requests library to send HTTP requests and process responses.
Parse and manipulate JSON data using Python.
Convert structured data into other formats, e.g., CSV.'''

'''
Instructions:
If not installed, install the requests library using pip: pip install requests.

Write a basic Python script to fetch posts from JSONPlaceholder using requests.get().

Create a function fetch_and_print_posts() that fetches all post from JSONPlaceholder.

Print the status code of the response i.e. Status Code: 200
If the request was sucessfull, parse the fetched data into a JSON object using the .json() method of the response object.
Iterate through the parsed JSON data and print out the titles of all the posts.

Create a function fetch_and_save_posts() that fetches all post from JSONPlaceholder.

If the request was sucessfull, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
Using Python’s csv module, write this data into a CSV file called posts.csv with columns corresponding to the dictionary keys.
'''


'''
Hints:
The requests.get() function returns a Response object, from which you can access various properties like status_code, headers, and methods like json().
When converting the parsed JSON data into a list of dictionaries, you might find list comprehensions useful for concise code.
The csv.DictWriter class can be a convenient way to write dictionaries to a CSV file, as it automatically handles headers based on dictionary keys.



Expected Output:
After the basic interaction script, you should have an output indicating a 200 status code, suggesting a successful GET request.
When parsing JSON data, you should see printed titles of the posts, e.g., “sunt aut facere repellat provident occaecati excepturi optio reprehenderit.”
After the data manipulation and conversion task, you should have a CSV file with columns id, title, and body. Each row in the CSV should correspond to a post from the fetched data.'''

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
