#
# Settings
#
from django.conf import settings

settings.configure(
    DEBUG = True,
    ALLOWED_HOSTS = ['localhost'],
    ROOT_URLCONF = 'foo',
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

#
# View (semelhante a um controller)
#
from django.conf.urls import url
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)

import django
django.setup()