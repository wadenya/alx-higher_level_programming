#!/bin/bash
#Only status code
curl -o /dev/null -s -w "%{http_code}\n" "$1"
