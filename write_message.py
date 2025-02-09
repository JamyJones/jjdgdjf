#!/bin/python3
import readline
#import subprocess
bio= True
#history file
filename="../gpt_hist.txt"

#load prompts history file
readline.read_history_file(filename)

msg=""
while True:
    usr = input("> ")
    if usr=='':
        break
    msg+=usr+"\n";
    readline.append_history_file(1,filename)

if bio==True:
    with open('msg.md','a') as fhand:
        fhand.write(msg)
elif bio==False:
    with open('msg.md','w') as fhand:
        fhand.write(msg)
        print("writing text to msg.txt...")
        fhand.close()

#script_path="routin.sh"
#subprocess.run(['bash',script_path],check=True)
