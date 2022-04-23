#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request


def mystatus(pagename):
    """ Python script that fetches in "url" page """
    with urllib.request.urlopen(pagename) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))


if __name__ == '__main__':
    mystatus('https://intranet.hbtn.io/status')
