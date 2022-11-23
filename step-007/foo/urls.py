from django.urls import path
from foo.views import index

urlpatterns = [
    path('', index),
]
