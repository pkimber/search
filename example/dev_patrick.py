# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'temp.db',                               # Or path to database file if using sqlite3.
        'USER': '',                               # Not used with sqlite3.
        'PASSWORD': '',                           # Not used with sqlite3.
        'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                          # Set to empty string for default. Not used with sqlite3.
    }
}

# install the simple engine (dev only)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
