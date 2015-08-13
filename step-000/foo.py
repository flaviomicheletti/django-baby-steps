#
# Settings
#

# from django.conf import settings

# settings.configure(
#     DEBUG = True,
#     ALLOWED_HOSTS = ['localhost'],
#     ROOT_URLCONF = '__main__',
#     MIDDLEWARE_CLASSES = (
#         'django.middleware.common.CommonMiddleware',
#         'django.middleware.csrf.CsrfViewMiddleware',
#         'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     ),
# )

import django
# django.setup()
print(django.get_version())

#
# Terminal
#
# import sys
# from django.core.management import execute_from_command_line
# execute_from_command_line(sys.argv)