#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
