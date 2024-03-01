#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - it handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    api_url = sys.argv[1]

    resp = requests.get(api_url)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
