import json
from django.test import TestCase

from chat.models import ChatMessage

class MessageTest(TestCase):

    def test_create(self):
        resp = self.client.post(
            '/message',
            '{"text": "ciao", "username": "pippo"}',
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            ChatMessage.objects.count(),
            1)
        # test message really exists
        resp = self.client.get('/message')
        self.assertEqual(resp.status_code, 200)
        messages = json.loads(resp.content)
        self.assertEqual(
            messages,
            [{'text': 'ciao', 'username': 'pippo'}])
