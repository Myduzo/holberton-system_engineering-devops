#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers.
"""
import requests

def number_of_subscribers(subreddit):
	"""method that returns the number of subs"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers={"User-agent": "Myduzo"}
	subs = requests.get(url, headers=headers).json()

	if subreddit is None:
		return 0

	try:
		total = subs["data"]["subscribers"]
		return total
	except KeyError:
		return 0
