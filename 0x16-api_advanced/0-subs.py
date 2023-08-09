#!/usr/bin/python3
"""
Reddit Subreddit Subscribers Count

This script queries the Reddit API to retrieve the number 
of subscribers for a given subreddit.If the subreddit is 
not valid or does not exist, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. If the subreddit is 
        invalid or does not exist, returns 0.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
