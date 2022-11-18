from django.urls import path
from roadrecord import views

urlpatterns = [
    path("", views.home, name="home"),
    path("roadrecord/<name>", views.hello_there, name="hello_there"),
]