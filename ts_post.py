import random
import urllib.request
import requests
import threading

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val = random.randint(1,30)
    url = 'https://api.thingspeak.com/update?api_key='
    key = 'W6WTKSSCWM7S2K8Z'
    header = '&field1={}'.format(val)
    new_url = url + key + header
    print(new_url)
    data = urllib.request.urlopen(new_url)
    print(data)

if __name__ == '__main__':
    thingspeak_post()
