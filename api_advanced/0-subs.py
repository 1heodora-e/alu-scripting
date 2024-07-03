#!/usr/bin/python3
"""Get the top ten hot posts of a subreddit"""

import json
import requests
import sys

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit"""
    if len(sys.argv) < 2:
        print(None)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        result = requests.get(url, headers=headers, allow_redirects=False)
        if result.status_code != 200:
            print(None)
            return
        body = json.loads(result.text)
        posts = body.get("data", {}).get("children", [])
        if not posts:
            print(None)
            return
        for post in posts:
            print(post.get("data", {}).get("title"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

