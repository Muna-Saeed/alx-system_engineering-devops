#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.
        after (str): Parameter used for pagination.

    Returns:
        list: List containing titles of all hot articles,
        or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()["data"]["children"]

            if not data:
                return hot_list

            hot_list.extend([post["data"]["title"] for post in data])
            new_after = data[-1]["data"]["name"]

            return recurse(subreddit, hot_list, new_after)
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
