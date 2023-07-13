from django.urls import path, include

urlpatterns = [
    path('', include("home.urls")),
    path("polls/", include("polls.urls")),
]
