#!/usr/bin/python

import json
import random as r
import requests


# URL Helper
def _url(path):
    return 'https://api.ciscospark.com/v1' + path

def get_rooms(at):
    headers = {'Authorization': at, 'content-type': 'application/json; charset=utf-8'}
    resp = requests.get(url=_url('/rooms'), headers = headers)
    file_dict = json.loads(resp.text)
    return file_dict

# function to post message
def post_file(at, roomId, markdown):
    headers = {'Authorization': at, 'content-type': 'application/json; charset=utf-8'}
    payload = {'roomId': roomId, 'markdown': markdown}
    resp = requests.post(url=_url('/messages'), json=payload, headers=headers)
    file_dict = json.loads(resp.text)
    file_dict['statuscode'] = str(resp.status_code)
    return file_dict


# access_token
a_t = "OGI3ZTZkODUtYTBmYS00NzNhLTk3YWYtNjkyYzgzOWE0Yzg3ZjdlZmQzN2EtNWYx"
a_t = "Bearer " + a_t


# Pull quotes from file`
quotes = []
lines = 0
with open("mike.txt", "r") as f:
    for line in f:
        quotes.append(line.strip('\n'))
        lines += 1

text = "**" + quotes[r.randrange(0, len(quotes), 1)] + "**"

print text

room_dict = get_rooms(a_t)[u'items']
print room_dict
for i in range(0,len(room_dict)):
    if room_dict[i][u'type'] == 'group':
        print(post_file(a_t, room_dict[i][u'id'], text))
        # print room_dict[i][u'id']
