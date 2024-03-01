#!/usr/bin/python3
"""this sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
it displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as r:
        print(r.read().decode("utf-8"))
