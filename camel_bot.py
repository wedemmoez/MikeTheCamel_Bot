#!/usr/bin/python

import json
import random as r
import requests
from credentials import *

# URL Helper
def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def get_rooms(at):
    headers = {'Authorization': at, 'content-type': 'application/json; charset=utf-8'}
    resp = requests.get(url=_url('/rooms'), headers = headers)
    file_dict = json.loads(resp.text)
    return file_dict

# function to post message
def post_file(at, roomId, markdown='', url=''):
    headers = {'Authorization': at, 'content-type': 'application/json; charset=utf-8'}
    payload = {'roomId': roomId}
    if markdown:
        payload['markdown'] = markdown
    if url:
        payload['files'] = url
    resp = requests.post(url=_url('/messages'), json=payload, headers=headers)
    file_dict = json.loads(resp.text)
    file_dict['statuscode'] = str(resp.status_code)
    return file_dict


# Pull images from file
images = []
lines = 0
with open("mike_img.txt","r") as g:
    for line in g:
        images.append(line.strip('\n'))
        lines += 1

image = images[r.randrange(0, len(images), 1)]

room_dict = get_rooms(token)[u'items']

for i in range(0,len(room_dict)):
    if room_dict[i][u'type'] == 'group':
        print(post_file(token, room_dict[i][u'id'], url = image))

#test function
# post_file(token, test_room, url = image)