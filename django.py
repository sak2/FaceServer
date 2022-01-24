#!/usr/bin/env python
import os
import sys
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.http import HttpResponse

filename = os.path.splitext(os.path.basename(__file__))[0]

urlpatterns = patterns('',
    url(r'^$', '%s.home' % filename, name='home'),
)

def home(request):
    return HttpResponse('hello')

if __name__ == "__main__":
    settings.configure(
        DEBUG=True,
        MIDDLEWARE_CLASSES = [],
        ROOT_URLCONF = filename
    )

    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], 'runserver'])