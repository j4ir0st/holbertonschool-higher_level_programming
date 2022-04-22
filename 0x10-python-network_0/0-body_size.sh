#!/bin/bash
sudo curl $1 -I -s | grep "Content-Length" | cut -d " " -f 2
