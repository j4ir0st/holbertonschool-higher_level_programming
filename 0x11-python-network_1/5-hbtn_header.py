#!/usr/bin/python3
"""
   sends a request to the URL and displays the value
   of the variable X-Request-Id in the response header
"""
import requests


def GETrequest(pagename):
    """ sends a request to the URL and displays the value of the variable """
    myrequest = requests.get(pagename)
    content = myrequest.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == '__main__':
    GETrequest('https://intranet.hbtn.io/status')
