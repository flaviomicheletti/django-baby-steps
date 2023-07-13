#
# Settings
#
from django.conf import settings

settings.configure(
    DEBUG = True,
    ALLOWED_HOSTS = ['localhost'],
    ROOT_URLCONF = '__main__',
    SECRET_KEY = 'django-insecure-u7_!un885z@tfdh^=leqq6y(v@hz)7*y8a7*dw+jxpf61*vajy',       
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

#
# View
#
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

urlpatterns = [
    path(r'', index),
]

#
# Terminal
#
if __name__ == "__main__":
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)