#!/usr/bin/python3
"""
   sends a request to the URL and displays the
   body of the response (decoded in utf-8).
"""
from urllib import request, error
from sys import argv


def showcontent(pagename):
    """ sends a request to the URL and displays the body of the response """
    try:
        with request.urlopen(pagename) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))


if __name__ == '__main__':
    url = argv[1]
    result = showcontent(url)
