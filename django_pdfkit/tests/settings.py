# -*- coding: utf-8 -*-
"""
    django_pdfkit.tests.settings
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Django test settings.
"""
from __future__ import absolute_import, print_function, unicode_literals
import os

DEBUG = True

ROOT_URLCONF = 'django_pdfkit.tests.urls'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

SECRET_KEY = 's3cr3t'

# Django replaces this, but it still wants it. *shrugs*
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = {}

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(os.path.dirname(__file__), 'templates')
    ],
    'OPTIONS': {
        'context_processors': [
            'django.core.context_processors.static',
            'django.core.context_processors.request',
        ]
    },
}]
