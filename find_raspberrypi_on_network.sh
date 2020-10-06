#!/bin/bash

sudo nmap -sP 10.0.0.0/24 | awk '/^Nmap/{ip=$NF}/B8:27:EB/{print ip}'
