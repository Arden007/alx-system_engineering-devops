#!/usr/bin/python3
""" raddit api"""
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        found_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    '''
    if after is None:
        word_list = [word.lower() for word in word_list]

    url = 'http://www.reddit.com/r/{}/hot.json?after={}'
    posts = requests.get(url.format(subreddit, after), headers={'User-agent': 'test45'})

    if posts.status_code == 200:
        posts = posts.json()['data']
        param = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if param is not None:
            count_words(subreddit, word_list, found_list, param)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
