#!/usr/bin/python3
""" Recursive function to fetch hot post titles from a Reddit subreddit """

import requests

# Global variable to keep track of the 'after' parameter for pagination
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively fetches and returns a list of titles of hot posts from a 
    subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot posts 
        from hot_list (list, optional): A list to accumulate hot post 
        titles. Defaults to an empty list.

    Returns:
        list or None: A list containing titles of hot posts, or None if 
        the subreddit is invalid or an error occurs.
    """
    global after
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    # Making a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False, params=params)

    if response.status_code == 200:
        # Extracting 'after' parameter for pagination
        data = response.json().get('data').get('after')
        if data is not None:
            after = data
            # Recursive call to continue fetching posts
            recurse(subreddit, hot_list)

        # Extracting post titles from the response
        titles = response.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))

        # Returning the list of hot post titles
        return hot_list
    else:
        # Returning None in case of invalid subreddit or other errors
        return None
