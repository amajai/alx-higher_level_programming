#!/bin/bash
# Content size of request
curl -sI "$1" | grep Content-Length | awk '{print $1}'
