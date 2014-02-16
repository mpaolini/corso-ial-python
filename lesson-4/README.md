# Python IAL chat server

A chat server and client that enables us to communicate during
the lessons

- user information on messages
- protection/auth

## Post messages

User opens his terminal, and calls this command:

    python chat_client.py post "ciao" "marco"

The client sends the message payload to the server.

If message is posted succesfully, print "OK" else print the error to console.

## Read messages

User opens his terminal and types:

    python chat_client.py read

The chat server responds with *all* the messages sorted in chronologycal order.

Messages also contain author info.


# Implementation

Server: a django project in dir
`lesson-4/server`

Client: uses python `requests` package and sits in `chat_client.py`


## Protocol

Http + JSON

post message:

    POST /message
    body: "ciao"

get messages:

    GET /message













