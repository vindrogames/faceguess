from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_room/", views.create_room, name="create_room"),
    path("join_room/", views.join_room, name="join_room"),
    path("upload/", views.upload_file, name="upload_file"),
    path("room/<number_room>/files/", views.view_files, name="list_files"),
    path("room/<number_room>/<user_id>", views.room, name="room"),    
]