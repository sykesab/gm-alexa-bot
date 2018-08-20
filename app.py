import os
import json
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

#group_id = '42721784'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    if data['name'] != 'test-alexa':
        msg = '{}, you sent "{}".'.format(data['name'], data['text'])
        send_message(msg)

    return "ok", 200

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id'    : os.getenv('GROUPME_BOT_ID'),
        'text'      : msg
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
#
#     data = request.get_json()
#
#     if data['text'][:5] == 'Alexa':
#         if data['name'] != 'test-alexa':
#             time.sleep(5)
#             send_message('yes')
#     else:
#         send_message('no call')
#
#     return "ok", 200
#
# def send_message(msg):
#     url = 'https://api.groupme.com/v3/groups/bots/post'
#
#     data = {
#         'bot_id' : bot_id,
#         'text' : msg,
#     }
#
#     rqst = Request(url, urlencode(data).encode())
#     print(rqst)
#     json = urlopen(rqst).read().decode()
