import os
import json
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'Alexa':
        if data['text'][:5].lower() == 'alexa':
            time.sleep(2)
            msg = 'ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito ───────────────⚪─────────────────── ◄◄⠀▐▐ ⠀►►⠀⠀ ⠀ 1:17 / 3:48 ⠀ ───○ 🔊⠀ ᴴᴰ ⚙ ❐ ⊏⊐'
            send_message(msg)
            despacito = 'https://youtu.be/kJQP7kiw5Fk?t=21s'
            time.sleep(3)
            send_message(despacito)

    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id'    : os.getenv('GROUPME_BOT_ID'),
        'text'      : msg
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
