import settings

#
# View
#
from django.conf.urls import url
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)

#
# Terminal
#
if __name__ == "__main__":
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)