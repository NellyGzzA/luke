# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status


class UserTest(TestCase):
    fixtures = ['users']

    def test_login_anonymous_user(self):
        url = reverse('users:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed('users/login.html')

    def test_login_authenticated_user(self):
        url = reverse('users:login')
        User = get_user_model()
        self.client.login(username='test', password='password')
        response = self.client.get(url, follow=True)
        user = User.objects.get(username='test')
        self.assertEqual(response.context['user'].email, user.email)
        self.assertRedirects(
            response,
            '/categories/',
            status_code=status.HTTP_302_FOUND
        )

    def test_login_with_invalid_credentials(self):
        url = reverse('users:login')
        form_data = {'username': 'test', 'password': 'password1'}
        response = self.client.post(url, form_data)
        self.assertEqual(response.context['user'], AnonymousUser())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Invalid credentials')

    def test_login_with_valid_credentials(self):
        url = reverse('users:login')
        form_data = {'username': 'test', 'password': 'password'}
        response = self.client.post(url, form_data)
        self.assertRedirects(
            response,
            '/categories/',
            status_code=status.HTTP_302_FOUND
        )

    def test_logged_user_logout(self):
        url = reverse('users:logout')
        self.client.login(username='test', password='password')
        response = self.client.post(url)
        self.assertRedirects(
            response,
            '/users/login',
            status_code=status.HTTP_302_FOUND
        )
