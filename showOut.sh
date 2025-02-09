#!/bin/bash
(unzip -p logs.zip "build/4_Run-gpt4free.txt" | sed 's/^2024[^ ]* //') > foo.txt
python edit.py
rm foo.txt
rm logs.zip
