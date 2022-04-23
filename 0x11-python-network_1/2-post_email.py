#!/usr/bin/python3
"""
  takes in a URL and an email, sends a POST request to the passed
  URL with the email as a parameter, and displays the body
  of the response (decoded in utf-8)
"""
from urllib import request, parse
from sys import argv


def POSTrequest(pagename, values, head=None):
    """  takes in a URL and an email, sends a POST request  """
    data = parse.urlencode(values)
    data = data.encode('ascii')
    if not head:
        myrequest = request.Request(pagename, data)
    else:
        myrequest = request.Request(pagename, data, head)

    with request.urlopen(myrequest) as response:
        body = response.read()
        return (body)


if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    result = POSTrequest(url, values)
    print(result.decode('utf-8'))
