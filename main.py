import requests
import json
from time import sleep
import random

Token = "tokenhere"



api_url_header = "https://discord.com/api/v9/"

Channelid = input("Channel Id :")



headers = {
    'authorization': Token,
    "content-type": "application/json",
}

comment = []
with open("bypass.txt", "r", encoding="utf-8_sig") as target:
    bypass = target.read().split("\n")

with open("spam.txt", "r", encoding="utf-8_sig") as target:
    spam = target.read().split("\n")

while True:
    params = {
        "content": random.choice(spam) +  " |" + " " + random.choice(bypass),
        "tts": False
    }
    create_message = requests.post(
        api_url_header + "channels/" + Channelid + "/messages", headers=headers, data=json.dumps(params))
    print(create_message)
    print(create_message.text)
    sleep(random.randint(1, 3))
