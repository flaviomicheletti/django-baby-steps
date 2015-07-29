SECRET_KEY = 'wsfkypx-ad1t*5^o@fdmaf2z-5*8vw91hmh)9787ys4(k!#!8l'
DEBUG = True
ALLOWED_HOSTS = ['localhost']
ROOT_URLCONF = 'foo.urls'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)