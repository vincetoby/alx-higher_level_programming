#!/usr/bin/python3
"""this displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    api_url = sys.argv[1]
    resp = requests.get(api_url)
    print(resp.headers.get("X-Request-Id"))
