from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        "polls/", include("polls.urls")
    ),  # include()は他のURLconfを参照することができる
    path("admin/", admin.site.urls),
]
