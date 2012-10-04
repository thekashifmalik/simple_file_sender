# Local settings for project.
import socket
import os
import django

DEBUG = TEMPLATE_DEBUG = True
STATIC_URL = '/static/'


# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__) + "/../../")

def relative_path(relative_root_path, target_file):
    return os.path.join(relative_root_path, target_file)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'simple_file_sender_db',                      # Or path to database file if using sqlite3.
        'USER': 'simple_file_sender_db_user',                      # Not used with sqlite3.
        'PASSWORD': 'simple_file_sender_db_password',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Amazon S3 setting
AWS_ACCESS_KEY_ID = 'AKIAI7EOYMFRURZPCUKA'
AWS_SECRET_ACCESS_KEY = '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'


# Set up Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'simple_file_sender_local_cache'
    }
}

# Browser ID settings
SITE_URL = 'http://localhost:8000'