from django.contrib import admin

# Register your models here.

from .models import Room, CustomUser

admin.site.register(Room)
admin.site.register(CustomUser)