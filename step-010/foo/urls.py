from django.conf.urls import url
from foobar.views import index

urlpatterns = (
    url(r'^$', index),
)