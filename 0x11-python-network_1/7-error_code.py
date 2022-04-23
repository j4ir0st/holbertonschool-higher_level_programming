#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


def showcontent(pagename):
    """ sends a request to the URL and displays the body of the response """
    myrequest = requests.get(pagename)
    if myrequest.status_code == 200:
        print(myrequest.text)
    else:
        print("Error code:", myrequest.status_code)


if __name__ == '__main__':
    url = argv[1]
    result = showcontent(url)
