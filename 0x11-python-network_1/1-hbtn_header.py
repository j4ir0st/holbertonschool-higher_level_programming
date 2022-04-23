#!/usr/bin/python3
"""
    sends a request to the URL and displays the value of the X-Request-Id
    variable found in the header of the response.
"""
import urllib.request
from sys import argv


def getvalueheaders(pagename, key):
    """  sends a request to the URL and displays the value  """
    with urllib.request.urlopen(pagename) as response:
        pageheaders = response.headers
        print(pageheaders.get(key))


if __name__ == '__main__':
    getvalueheaders(argv[1], 'X-Request-Id')
