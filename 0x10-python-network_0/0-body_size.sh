#!/bin/bash
# sends a request to that URL and displays the size of the body of the response
sudo curl $1 -I -s | grep "Content-Length" | cut -d " " -f 2
