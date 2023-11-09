#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Find hot articles of a subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyUserAgent"}
    params = {"after": after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list += [post["data"]["title"] for post in children]
        after = data.get("after")

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except requests.exceptions.RequestException:
        return hot_list
