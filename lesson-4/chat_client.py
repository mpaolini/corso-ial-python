import requests
import sys
import json

HOST = 'localhost:8000'

# http://python-requests.org/

# post new message
def post_new_message(text, username, password):
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


import argparse

parser = argparse.ArgumentParser('chat client')
parser.add_argument('command')
parser.add_argument('--message')
parser.add_argument('--user')
parser.add_argument('--password')
args = parser.parse_args()


if args.command == 'post':
    post_new_message(args.message, username=args.user,
                     password=args.password)
elif args.command == 'read':
    read_messages()
else:
    print 'Errore'
    
