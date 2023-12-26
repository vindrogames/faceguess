from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=30)
    identifier = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class CustomUser(models.Model):    
    username = models.CharField(max_length=30)
    is_admin = models.BooleanField(default = False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='users')
    def __str__(self):
        return self.username