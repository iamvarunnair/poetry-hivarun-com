#!/usr/bin/env python
import json
import random
import sys
from pathlib import Path

from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.shortcuts import redirect, render
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

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '*']
# ALLOWED_HOSTS = ['poetry.hivarun.com', 'www.poetry.hivarun.com']

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
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
                ],
            },
        },
    ],
)


# def index(request):
#     return HttpResponse('<html><head></head><body><h1>Hello World</h1></body></html>')

"""
Views
1:  Home
2:  Index
3:  All Poems or Search Poem
4:  Single Poem or Random Poem
5:  Other favourites
6:  Categories
7: About Author
"""


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
            # return render(request, 'failure.html', {'message': ex})
            return render(request, 'failure.html')


def index(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        try:
            with open('book.json', "r") as file:
                output_json = json.loads(file.read())
            if output_json == '':
                raise Exception('Empty file.')
            back_url = request.GET.get('back', 'home')
            return render(request, 'poems_index.html', {'status': 0, 'message': 'Worked fine.', 'payload': output_json['indexArray'], 'back_url': back_url})
        except Exception as ex:
            # return render(request, 'failure.html', {'message': ex})
            return render(request, 'failure.html')


def all_poems(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        try:
            with open('book.json', "r") as file:
                output_json = json.loads(file.read())
            if output_json == '':
                raise Exception('Empty file.')
            back_url = request.GET.get('back', 'home')
            return render(request, 'all_poems.html', {'status': 0, 'message': 'Worked fine.', 'payload': output_json['poemsArray'], 'back_url': back_url})
        except Exception as ex:
            # return render(request, 'failure.html', {'message': ex})
            return render(request, 'failure.html')


def single_poem(request, poem_index):
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        try:
            with open('book.json', "r") as file:
                output_json = json.loads(file.read())
            if output_json == '':
                raise Exception('Empty file.')
            back_url = request.GET.get('back', 'home')
            random_button = request.GET.get('random', 0)
            return render(request, 'single_poem.html', {'status': 0, 'message': 'Worked fine.', 'payload': output_json['poemsArray'][int(poem_index) - 1], 'back_url': back_url, 'random_button': int(random_button)})
        except Exception as ex:
            return render(request, 'failure.html', {'message': ex})
            # return render(request, 'failure.html')


def poem_random(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'GET':
        try:
            with open('book.json', "r") as file:
                output_json = json.loads(file.read())
            if output_json == '':
                raise Exception('Empty file.')
            return redirect('/'+str(random.randint(0, len(output_json['poemsArray']) - 1))+'?back=home&random=1')
        except Exception as ex:
            return render(request, 'failure.html', {'message': ex})
            # return render(request, 'failure.html')


def page_not_found(request):
    return render(request, '404.html')


urlpatterns = (
    re_path(r'^$', home, name='home'),
    re_path(r'^index$', index, name='index'),
    re_path(r'^all$', all_poems, name='poems'),
    re_path(r'^(?P<poem_index>\d+)$', single_poem, name='poem'),
    re_path(r'^any', poem_random, name='random'),
    re_path(r'^google-auth$', google_auth, name='google_auth'),
    re_path(r'^update-from-doc$', update_json_file, name='update'),
    re_path(r'^$', page_not_found, name='page_not_found'),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
