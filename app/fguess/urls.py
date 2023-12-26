from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_room/", views.create_room, name="create_room"),
    path("join_room/", views.join_room, name="join_room"),
    path("room/<number_room>", views.room, name="room"),
]