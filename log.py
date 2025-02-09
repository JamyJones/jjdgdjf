#!/bin/python3
import requests
import time
import json


REPO="chatGpt-app"
OWNER="john4650-hub"
URL = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs?per_page=1&page=1"
token=""
with open("../.secrets/git_token","r") as tk:
    token=tk.read().strip()
def makeReq(url):
    return requests.get(url,headers={
   'Accept': 'application/vnd.github+json',
   'Authorization':f'Bearer {token}',
   'X-GitHub-Api-Version':'2022-11-28'
    })

res = makeReq(URL)

URL = res.json().get('workflow_runs')[0].get('logs_url')
res = makeReq(URL)
with open('logs.zip', 'wb') as fn:
    for chunk in res.iter_content(chunk_size=128):
        fn.write(chunk)
