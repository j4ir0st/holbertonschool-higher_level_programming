#!/usr/bin/python3
"""
   script that fetches https://intranet.hbtn.io/status
"""
import requests


def GETrequest(pagename):
    """ script that fetches https://intranet.hbtn.io/status """
    myrequest = requests.get(pagename)
    content = myrequest.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == '__main__':
    GETrequest('https://intranet.hbtn.io/status')
