from django.conf.urls import url
from foo.views import index

urlpatterns = (
    url(r'^$', index),
)