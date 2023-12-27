from django.contrib import admin

# Register your models here.

from .models import Room, CustomUser, UploadedFile

admin.site.register(Room)
admin.site.register(CustomUser)
admin.site.register(UploadedFile)