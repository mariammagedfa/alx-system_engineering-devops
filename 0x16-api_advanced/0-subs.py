#!/usr/bin/python3
"""Contains a function that returns number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data').get('subscribers')
            return int(subscribers)
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
