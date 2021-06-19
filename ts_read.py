import random
import urllib.request
import requests
import threading
import json

def thingspeak_read():
    URL = 'https://api.thingspeak.com/channels/1027157/feeds.json?api_key='
    KEY = 'SCOJSAAIZA3IO0BF'
    HEADER = ''
    NEW_URL = URL + KEY + HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    print(get_data)
    channel_id = get_data['channel']['id']
    print(channel_id)

    feild_1 = get_data['feeds']
    print(feild_1)

    t=[]
    for i in feild_1:
        print(i['field1'])
        t.append(i['field1'])
    print(t)


if __name__ == '__main__':
    thingspeak_read()
