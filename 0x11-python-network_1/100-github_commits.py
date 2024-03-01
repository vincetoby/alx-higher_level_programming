#!/usr/bin/python3
""" this lists the 10 most recent commits on a given GitHub repo.
Usage: ./100-github_commits.py <repository name> <repository owners username>
"""
import sys
import requests


if __name__ == "__main__":
    api_url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    gitresponse = requests.get(api_url)
    commits = gitresponse.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
