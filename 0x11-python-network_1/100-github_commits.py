#!/usr/bin/python3
"""
  script that takes your 10 first GitHub commits per request
"""
import requests
from sys import argv


def commitsGitHub(repo, ownr):
    """ get GitHub commits """
    gitApi = 'https://api.github.com/repos/'
    gitApi = gitApi + '{}/{}/commits?per_page={}'.format(ownr, repo, 10)
    request = requests.get(gitApi)
    tojson = request.json()
    for commit in tojson:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name"))
        )


if __name__ == '__main__':
    urlapi = 'https://api.github.com/user'
    repo = argv[1]
    ownr = argv[2]
    commitsGitHub(repo, ownr)
