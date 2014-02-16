import requests
import sys
import json

HOST = '158.110.47.12:8000'


# post new message
def post_new_message(text, username):
    resp = requests.post(
        'http://{}/message'.format(HOST),
        json.dumps({'text': text, 'username': username}))
    if resp.status_code == 200:
        print 'OK'
    else:
        print 'ERROR'
        print resp.content

def read_messages():
    resp = requests.get(
        'http://{}/message'.format(HOST))
    if resp.status_code == 200:
        messages = json.loads(resp.content)
        print 'Messages:'
        for message in messages:
            print '{username}: {text}'.format(**message)
            # .format(
            #    username=message['username'],
            #    text=message['text'])
    else:
        print 'ERROR'


if sys.argv[1] == 'post':
    post_new_message(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'read':
    read_messages()
else:
    print 'Errore'
    
