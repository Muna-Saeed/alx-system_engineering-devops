#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Parameter used for pagination.
        count_dict (dict): Dictionary to store the count of each keyword.

    Returns:
        None
    """
    if count_dict is None:
        count_dict = {}

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
                sorted_results = sorted(
                        count_dict.items(), key=lambda x: (-x[1], x[0])
                        )
                for keyword, count in sorted_results:
                    print(f"{keyword}: {count}")
                return

            for post in data:
                title = post["data"]["title"].lower()
                for word in word_list:
                    if f" {word.lower()} " in f" {title} ":
                        count_dict[word.lower()] = count_dict.get(
                                word.lower(), 0) + 1

            new_after = data[-1]["data"]["name"]
            return count_words(subreddit, word_list, new_after, count_dict)
        else:
            return
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print(
                "Ex: {} programming 'python java javascript'".format(
                    sys.argv[0]
                    )
                )
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
