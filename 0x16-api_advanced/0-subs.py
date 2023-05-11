#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """
    Returns:
         number of subscribers (total subscribers).
         If an invalid subreddit return 0.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)