#!/usr/bin/python3
"""Reddit Top Ten Hot Posts"""


import requests


def top_ten(subreddit):
    """
    Retrieve and print the titles of the first 10
    hot posts for a given subreddit.

    This function queries the Reddit API using the
    '/hot.json' endpoint to obtain the titles of
    the first 10 hot posts from the specified subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
        return
