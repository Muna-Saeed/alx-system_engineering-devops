#!/usr/bin/python3
"""
0-subs
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    user = {'User-Agent': 'Munawara'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()

    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
