# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status


class CategoriesTests(TestCase):
    fixtures = ['users']

    def test_anonymous_user(self):
        url = reverse('categories:index')
        response = self.client.get(url)
        self.assertRedirects(
            response,
            '/users/login?next=/categories/',
            status_code=status.HTTP_302_FOUND
        )

    def test_logged_user(self):
        url = reverse('categories:index')
        user = User.objects.get(pk=1)
        self.client.login(username=user.username, password='password')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.context['user'].email, user.email)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
