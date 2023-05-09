#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ Returns a list of titles of all hot posts on a given subreddit. """
    global after
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)

    if response.status_code == 200:
        data = response.json().get('data').get('after')
        if data is not None:
            after = data
            recurse(subreddit, hot_list)
        titles = response.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
