import g4f

txt = ""
with open("../qns.txt", "r") as fhand:
    txt = fhand.read().split("NQ")
    fhand.close()

g4f.debug.logging = False  # Enable logging
g4f.check_version = False  # Disable automatic version checking
for qn in txt:
    print("##" + qn)
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4, messages=[{"role": "user", "content": qn}]
    )

    for message in response:
        print(message, end="")
    print("---")
