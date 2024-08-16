#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    # Define the base URL for Reddit's API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid being blocked
    headers = {'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'}
    
    try:
        # Make the GET request to the API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code indicates success
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 if the subreddit is invalid or any other error occurs
            return 0
    except requests.RequestException:
        # Handle any request-related exceptions
        return 0
