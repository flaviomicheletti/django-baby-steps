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