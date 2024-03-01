#!/usr/bin/python3
"""this sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - it displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    api_url = sys.argv[1]
    val = {"email": sys.argv[2]}

    resp = requests.post(api_url, data=val)
    print(resp.text)
