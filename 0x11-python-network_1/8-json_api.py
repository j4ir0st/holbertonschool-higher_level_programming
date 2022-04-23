#!/usr/bin/python3
"""
  sends a POST request to http://0.0.0.0:5000/search_user
  with the letter as a parameter.
"""
import requests
from sys import argv


def POSTrequestJson(pagename, values, head=None):
    """ sends a POST request to http://0.0.0.0:5000/search_user """
    if not head:
        myrequest = requests.post(pagename, data=values)
    else:
        myrequest = requests.post(pagename, data=values, headers=head)
    try:
        myjson = myrequest.json()
        if not myjson:
            return ("No result")
        else:
            return ("[{}] {}".format(myjson.get('id'), myjson.get('name')))
    except BaseException:
        return ("Not a valid JSON")


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ''}
    if len(argv) >= 2:
        values['q'] = argv[1]
    result = POSTrequestJson(url, values)
    print(result)
