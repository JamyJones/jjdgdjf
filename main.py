from g4f.client import Client
import wave
import subprocess
import requests
from markdown import markdown
from bs4 import BeautifulSoup
import base64
import json


client = Client()
REPO = "Pastebin"
OWNER = "John4650-hub"
PATH = "paste.md"
bio = False
txt = ""
sysMsg = ""
not_allowed=[]
with open("notAllowed.txt","r") as fhand:
    not_allowed=[i.strip() for i in fhand.readlines()]
with open("msg.md", "r") as fhand:
    txt = fhand.read()
    fhand.close()

with open("system.md","r") as fhand:
    sysMsg = fhand.read()

MSG = ""
if bio == True:
    with open("bioTeacdnher.txt", "r") as ppt:
        MSG = ppt.read() + txt
elif bio == False:
    MSG = txt
#g4f.debug.logging = False  # Enable logging
#g4f.check_version = False  # Disable automatic version checking
msgGot = False
ans = ""

# api = TTS("tts_models/en/ljspeech/speedy-speech").to("cpu")
while msgGot == False:
    response = client.chat.completions.create(
            model="gpt-4o", messages=[{"role":"system", "content":sysMsg},{"role": "user", "content": MSG}]
    )
    if response.choices[0].message.content not in not_allowed:
        msgGot = True
    if msgGot == True:
        c = base64.b64encode(bytes(response.choices[0].message.content
, "utf-8")).decode("utf-8")
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}"

        # Set up headers for the request
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f'Bearer {base64.b64decode("Z2hwX1ZSc01RdGxDMHIydzVPTEt3aEJ0cGhSS09BU0h1czBWUHBTQw==".encode("ascii")).decode("ascii")}',
            "X-GitHub-Api-Version": "2022-11-28",
        }

        # Fetch the current content of the file to get the SHA
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            sha_ = response.json()["sha"]
            print(sha_)
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
        #ans += response
        break
# input_=ffmpeg.input("output.wav")
# out_=ffmpeg.output(input_,"output.flac")
saved = False
if bio == True:
    # Replace with your actual keys
    client_key = "fFsTHf3mTrxe9UkRJg1gQReear8kttqa"
    api_key = "nw1MXEELguRgemTT9fxg6UmpUVQ1Z66d"
    # Data to be sent
    html = markdown(ans)
    text = "".join(BeautifulSoup(html).findAll(text=True))
    res = text.split(".")
    fwavs = []
    n = 1
    for talk in res:
        fname = f"output{n}.wav"
        if len(talk) < 5:
            continue
        else:
            data = {"voiceId": 1017, "text": talk}

            # Headers with your API keys
            headers = {
                "X-Client-Key": client_key,
                "X-Api-Key": api_key,
                "Content-Type": "application/json",  # Optional, but recommended
            }

            # Send POST request
            response = requests.post(
                "https://api.gemelo.ai/v1/tts/convert", headers=headers, json=data
            )

            # Check for successful response
            if response.status_code == 200:
                # Write the audio content to a file
                fname = f"output{n}.wav"
                with open("out_/" + fname, "wb") as f:
                    f.write(response.content)
                fwavs.append(fname)
                n += 1
            else:
                print(f"Error converting text: {response}")
    data = []
    outfile = "output.wav"
    for fwv in fwavs:
        w = wave.open("out_/" + fwv, "rb")
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open(outfile, "wb")
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
    saved = True
if saved == True:
    subprocess.run("ls -lh", shell=True)
    subprocess.run(
        f"ffmpeg -i output.wav -acodec libmp3lame -b:a 50k output.mp3", shell=True
    )
    subprocess.run("clear", shell=True)
# if bio == False:
#    subprocess.run("touch output.mp3", shell=True)
# subprocess.run("echo msg here", shell=True)

# print(ans)
