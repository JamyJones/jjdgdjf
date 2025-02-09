from g4f.client import Client
import requests
from bs4 import BeautifulSoup
import base64
import json
import time
import os
import datetime

client = Client()
REPO = "Pastebin"
OWNER = "John4650-hub"
PATH = "paste.md"
PATH_RD = "msg.txt"
bio = False
token = os.getenv("GITHUB_TOKEN")
sysMsg = ""
not_allowed = []
with open("notAllowed.txt", "r") as fhand:
    not_allowed = [i.strip() for i in fhand.readlines()]

with open("system.md", "r") as fhand:
    sysMsg = fhand.read()


def getMessage():
    msg = requests.get(
        "https://raw.githubusercontent.com/JamyJones/jjdgdjf/refs/heads/gemelo/msg.md"
    )
    return msg.text


def runChat(MSG):
    """
    run chat.
    """
    msgGot = False
    while not msgGot:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": sysMsg},
                {"role": "user", "content": MSG},
            ],
        )
        if response.choices[0].message.content not in not_allowed:
            msgGot = True
        if msgGot == True:
            c = base64.b64encode(
                bytes(response.choices[0].message.content, "utf-8")
            ).decode("utf-8")
            url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"

            # Set up headers for the request
            headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
            }

            # Fetch the current content of the file to get the SHA
            response = requests.get(url, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                sha_ = response.json()["sha"]
            else:
                print(f"Error fetching file: {response.status_code} - {response.text}")
                exit()

            # Prepare the data for the update
            data = {
                "message": "done",
                "content": c,
                "sha": sha_,
            }

            # Update the file content using PUT request
            p = requests.put(url, headers=headers, json=data)

            # Check if the u:pdate was successful
            if p.status_code == 200:
                print("File updated successfully.")
            else:
                print(f"Error updating file: {p.status_code} - {p.text}")
            break


if __name__ == "__main__":
    prev_msg = ""
    new_msg = ""
    while True:
        with open("msg.md", "r") as fhand:
            new_msg = getMessage()
            fhand.close()
        if new_msg == "exit":
            break
        elif new_msg == prev_msg:
            continue
        else:
            runChat(new_msg)
            prev_msg = new_msg
        time.sleep(10)
        current_time = datetime.now()
        print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
