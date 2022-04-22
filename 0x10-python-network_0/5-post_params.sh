#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
sudo curl $1 -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
