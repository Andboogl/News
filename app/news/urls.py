"""Urls"""


from django.urls import path
from news import views


app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("info/", views.info, name="info")
]
