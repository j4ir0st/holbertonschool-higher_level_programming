#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
sudo curl $1 -I DELETE -s | grep "Allow" | cut -d ":" -f 2-
