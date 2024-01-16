#!/usr/bin/python3
"""Function that queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
