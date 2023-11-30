#!/bin/bash
# Content size of request
curl -sw '%{size_download}\n' "$1"
