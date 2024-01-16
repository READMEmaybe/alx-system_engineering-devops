#!/usr/bin/python3
""" 100-count.py """
import requests


def count_words(subreddit, word_list, after="", word_dic={}):
    """ count_words """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)"}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        for word in word_list:
            word = word.lower()
            if word not in word_dic:
                word_dic[word] = 0
        for child in response.json().get("data").get("children"):
            title = child.get("data").get("title").lower().split()
            for word in word_list:
                word = word.lower()
                word_dic[word] += title.count(word)
            after = response.json().get("data").get("after")
        if after is None:
            for key, value in sorted(word_dic.items(),
                                     key=lambda x: (-x[1], x[0])):
                if value != 0:
                    print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dic)
    else:
        return
