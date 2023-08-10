#!/usr/bin/python3
import requests
from collections import Counter
"""fetches and counts occurrences of given keywords in hot article 
titles from a Reddit subreddit.
"""


def count_words(subreddit, word_list, after=None, word_counter=None):
    """
    Recursively fetches and counts occurrences of given keywords in
    hot article titles from a Reddit subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to retrieve hot
        articles from.word_list (list): A list of keywords to count 
        occurrences of in article titles.after (str, optional):
        The 'after' parameter for pagination.
        Defaults to None.word_counter (collections.Counter, optional)
        : A counter to keep track of keyword occurrences.
        Defaults to None.

    Returns:
        None
    """
    if word_counter is None:
        word_counter = Counter()

    headers = {'User-Agent': 'Your User Agent'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 25}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    word_counter[word.lower()] += 1

        after = data['data']['after']

        if after:
            return count_words(subreddit, word_list, after, word_counter)
        else:
            sorted_counts = sorted(word_counter.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
