#!/usr/bin/env python3

import os
import requests

source_dir = "/data/feedback/"
files = os.listdir(source_dir)

def readlines(file):
    with open(source_dir + file) as f:
        lines = f.read().splitlines()
    return lines

feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
    lines = readlines(file)
    feedback.append(dict(zip(keys, lines)))

url = "http://localhost/feedback"

for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error : {response.status_code}")