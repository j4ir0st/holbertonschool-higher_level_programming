#!/usr/bin/python3
"""
   sends a request to the URL and displays the value
   of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


def getvalueheaders(pagename, key):
    """ sends a request to the URL and displays the value of the variable """
    myrequest = requests.get(pagename)
    myheaders = myrequest.headers
    print(myheaders.get(key))


if __name__ == '__main__':
    getvalueheaders(argv[1], 'X-Request-Id')
