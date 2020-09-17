#!/usr/bin/python3
"""
function that prints the titles of the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """method that returns the titles of hot posts"""
    url = "http://reddit.com/r/{}".format(subreddit)\
          + "/hot.json?limit=10"
    headers = {"User-agent": "Myduzo"}
    hot = requests.get(url, headers=headers).json()

    try:
        posts = hot["data"]["children"]

        for post in posts:
            print(post["data"]["title"])
    except KeyError:
        print(None)
