from django.shortcuts import render
from django.http import HttpResponse
from chat.models import ChatMessage
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def message(request):

    try:
        username = request.META['HTTP_X_USERNAME']
        password = request.META['HTTP_X_PASSWORD']
    except KeyError:
        return HttpResponse(status=401)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(status=401)

    if not user.check_password(password):
        return HttpResponse(status=401)

    if request.method == 'POST':
        # fetch message body
        body = request.body
        message = json.loads(body)  # deserialize
        chat_message = ChatMessage(
            text=message['text'],
            username=user.username)
        chat_message.save()
        return HttpResponse('')
    else:
        chat_messages = ChatMessage.objects.all()
        text_list = [{'text': x.text, 'username': x.username} for x in chat_messages]
        # serialize
        resp_body = json.dumps(text_list)
        return HttpResponse(resp_body)


