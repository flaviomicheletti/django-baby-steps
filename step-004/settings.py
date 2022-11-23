from django.conf import settings

settings.configure(
    DEBUG = True,
    ALLOWED_HOSTS = ['localhost', 'testserver'],
    ROOT_URLCONF = 'foo',
    SECRET_KEY = 'django-insecure-u7_!un885z@tfdh^=leqq6y(v@hz)7*y8a7*dw+jxpf61*vajy',    
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)