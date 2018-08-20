import os
import json
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

bot_id = '057d3858182e8a31f234c38eaa'
group_id = '42721784'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['text'][:5] == 'Alexa':
        if data['name'] != 'test-alexa':
            time.sleep(5)
            send_message('Now playing: Despacito')
    else:
        send_message('no call')

    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/groups/bots/post'

    data = {
        'bot_id' : bot_id,
        'text' : msg,
    }

    rqst = Request(url, urlencode(data).encode())
    print(rqst)
    json = urlopen(rqst).read().decode()
