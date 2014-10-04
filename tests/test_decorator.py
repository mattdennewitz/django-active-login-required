from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.test import Client, TestCase


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.password = '...'

        # create an active user
        self.active_user = User(username='active_user', is_active=True)
        self.active_user.set_password(self.password)
        self.active_user.save()

        # create an inactive user
        self.inactive_user = User(username='inactive_user', is_active=False)
        self.inactive_user.set_password(self.password)
        self.inactive_user.save()

    def test_anonymous_user_redirection(self):
        expected_url = '/accounts/login/?next=/test_view_a/'

        resp = self.client.get('/test_view_a/')

        self.assertRedirects(resp, expected_url,
                             fetch_redirect_response=False)

    def test_inactive_user(self):
        expected_url = '/accounts/login/?next=/test_view_a/'

        self.client.login(username=self.inactive_user,
                          password=self.password)

        resp = self.client.get('/test_view_a/')

        self.assertRedirects(resp, expected_url,
                             fetch_redirect_response=False)

    def test_active_user(self):
        self.client.login(username=self.active_user,
                          password=self.password)

        resp = self.client.get('/test_view_a/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content, settings.AFFIRMATIVE)
