#!/usr/bin/python3
"""
   sends a request to the URL and displays the value
   of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


def POSTrequest(pagename, values, head=None):
    """ sends a request to the URL and displays the value of the variable """
    if not head:
        myrequest = requests.post(pagename, values)
    else:
        myrequest = requests.post(pagename, values, headers=head)
    return (myrequest.text)


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    result = POSTrequest(url, values)
    print(result)
