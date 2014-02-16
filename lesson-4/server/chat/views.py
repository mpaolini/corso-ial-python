from django.shortcuts import render
from django.http import HttpResponse
from chat.models import ChatMessage
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def message(request):
    if request.method == 'POST':
        # fetch message body
        body = request.body
        message = json.loads(body)  # deserialize
        chat_message = ChatMessage(
            text=message['text'],
            username=message['username'])
        chat_message.save()
        return HttpResponse('')
    else:
        chat_messages = ChatMessage.objects.all()
        text_list = [{'text': x.text, 'username': x.username} for x in chat_messages]
        # serialize
        resp_body = json.dumps(text_list)
        return HttpResponse(resp_body)


