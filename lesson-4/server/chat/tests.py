import json
from django.test import TestCase

from chat.models import ChatMessage

class MessageTest(TestCase):

    def test_create_noauth(self):
        resp = self.client.post(
            '/message',
            '{"text": "ciao"}',
            content_type='application/json')
        self.assertEqual(resp.status_code, 401)

    def test_read_noauth(self):
        resp = self.client.get('/message')
        self.assertEqual(resp.status_code, 401)

    def test_create_wrong_pass(self):
        from django.contrib.auth.models import User
        user = User(username='pippo',
                    email='pippo@example.com')
        user.set_password('pass')
        user.save()
        resp = self.client.post(
            '/message',
            '{"text": "ciao"}',
            HTTP_X_USERNAME='pippo',
            HTTP_X_PASSWORD='xxx',
            content_type='application/json')
        self.assertEqual(resp.status_code, 401)

    def test_create_wrong_user(self):
        from django.contrib.auth.models import User
        user = User(username='pippo',
                    email='pippo@example.com')
        user.set_password('pass')
        user.save()
        resp = self.client.post(
            '/message',
            '{"text": "ciao"}',
            HTTP_X_USERNAME='pluto',
            HTTP_X_PASSWORD='xxx',
            content_type='application/json')
        self.assertEqual(resp.status_code, 401)

    def test_create(self):
        from django.contrib.auth.models import User
        user = User(username='pippo',
                    email='pippo@example.com')
        user.set_password('pass')
        user.save()
        resp = self.client.post(
            '/message',
            '{"text": "ciao"}',
            HTTP_X_USERNAME='pippo',
            HTTP_X_PASSWORD='pass',
            content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            ChatMessage.objects.count(),
            1)
        # test message reallpy exists
        resp = self.client.get('/message',
                               HTTP_X_USERNAME='pippo',
                               HTTP_X_PASSWORD='pass')
        self.assertEqual(resp.status_code, 200)
        messages = json.loads(resp.content)
        self.assertEqual(
            messages,
            [{'text': 'ciao', 'username': 'pippo'}])
