#!/usr/bin/python3
"""this sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
 it Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as r:
            print(r.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
