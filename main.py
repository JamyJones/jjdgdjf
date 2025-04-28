from g4f.client import Client
import requests
from bs4 import BeautifulSoup
import base64
import json
import time
import os
from datetime import datetime


client = Client()
REPO = "Pastebin"
REPO_R = "jjdgdjf"
OWNER = "JamyJones"
PATH = "paste.md"
PATH_R = "msg.md"
token = os.getenv("GITHUB_TOKEN")
print(len(token))
sysMsg = ""
not_allowed = []
with open("notAllowed.txt", "r") as fhand:
    not_allowed = [i.strip() for i in fhand.readlines()]

with open("system.md", "r") as fhand:
    sysMsg = fhand.read()


def getMessage():
    url = f"https://api.github.com/repos/{OWNER}/{REPO_R}/contents/{PATH_R}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json().get("content", "")
        decoded_content = base64.b64decode(content).decode("utf-8")
        return decoded_content.strip()
    else:
        print(f"Failed to retrieve file: {response.status_code}")
        return "exit"


def runChat(system_prompt, user_message):
    """
    run chat.
    """
    msgGot = False
    while not msgGot:
        if system_prompt == "None":
            system_prompt = sysMsg
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
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

            # Check if the update was successful
            if p.status_code == 200:
                print("File updated successfully.")
            else:
                print(f"Error updating file: {p.status_code} - {p.text}")
            break


if __name__ == "__main__":
    prev_msg = ""
    while True:
        new_msg = json.loads(getMessage())
        system_prompt = new_msg["prompt"]
        user_message = new_msg["user_message"]
        if user_message == "exit":
            break
        elif user_message == prev_msg:
            time.sleep(20)
            current_time = datetime.now()
            print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            runChat(system_prompt, user_message)
            prev_msg = user_message
