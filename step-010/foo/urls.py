from django.urls import path
from foobar.views import index

urlpatterns = [
    path('', index),
]
