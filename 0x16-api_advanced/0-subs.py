#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    user_agent = 'userAgent'
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return 0
    data = req.json()['data']
    pages = data['children']
    page_data = pages[0]['data']
    return page_data['subreddit_subscribers']
