#!/usr/bin/env python
import json
import sys
from pathlib import Path

from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import re_path

"""
 Usage:
    1. download this file tinydjango.py 
    2. run `pip install django`
    3. run `python tinydjango.py runserver 8000`
    4. open a browser and head to http://localhost:8000 
    5. bananas
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

DEBUG = False

SECRET_KEY = '41+_$!j&y@zr#9cxdp6m9o3j&6dnk__bq*deii)5w6w744e7a#'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        # 'django.contrib.auth',
        'django.contrib.contenttypes',
        # 'django.contrib.staticfiles',
    ],
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR/'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    # 'django.contrib.auth.context_processors.auth',
                    # 'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
)


# def index(request):
#     return HttpResponse('<html><head></head><body><h1>Hello World</h1></body></html>')


def google_auth(request):
    if request.method == 'GET':
        return render(request, 'google_auth.html')


def update_json_file(request):
    if request.method == 'POST':
        try:
            output_json = json.loads(request.body.decode('utf-8'))['inputJson']
            with open('book.json', "w") as file:
                json.dump(output_json, file)
            return HttpResponse(json.dumps({'status': 0, 'message': 'Worked fine.'}))
        except Exception as ex:
            return HttpResponse(json.dumps({'status': 1, 'message': 'Error while updating json.'}))


def fetch_book_preview(request):
    if request.method == 'GET':
        try:
            with open('book.json', "r") as file:
                output_json = json.loads(file.read())
            if output_json == '':
                raise Exception('Empty file.')
            return render(request, 'book_preview.html', {'status': 0, 'message': 'Worked fine.', 'payload': output_json})
        except Exception as ex:
            return render(request, 'failure.html')


def home(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        try:
            with open('book.json', "r") as file:
                output_json = json.loads(file.read())
            if output_json == '':
                raise Exception('Empty file.')
            zipped = zip(*(iter(output_json['poemsArray']),) * 5)
            list_zipped = list(zipped)
            return render(request, 'home.html', {'status': 0, 'message': 'Worked fine.', 'payload': {'title': output_json['titlePage']['title'], 'sub_heading': output_json['titlePage']['subHeadings'][0], 'poems_list': list_zipped[:3]}})
        except Exception as ex:
            return render(request, 'failure.html')


urlpatterns = (
    re_path(r'^$', fetch_book_preview, name='preview'),
    re_path(r'^google-auth$', google_auth, name='google_auth'),
    re_path(r'^update-from-doc$', update_json_file, name='update'),
    re_path(r'^home$', home, name='home'),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
