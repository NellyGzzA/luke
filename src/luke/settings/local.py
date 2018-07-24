# -*- coding: utf-8 -*-
"""
Django development settings for luke project.
"""
from . import *  # noqa


# Debug
DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'luke',
        'USER': 'vagrant'
    }
}


# Debug toolbar
INTERNAL_IPS = ('127.0.0.1',)
