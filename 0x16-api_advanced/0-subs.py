#!/usr/bin/python3
""" Function queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to subreddit,
        or 0 when subreddit requested is invalid"""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
