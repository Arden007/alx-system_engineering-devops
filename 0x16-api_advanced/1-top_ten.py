#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed for a given subreddit. 
        If not a valid subreddit, print None.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)

    if response.status_code == 400:
        print(None) 
        return   
    else:
        titles = response.json().get('data').get('children')
        for title in titles:
            print(title.get('data').get('title'))
