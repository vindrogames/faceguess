from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from fguess.models import Room, CustomUser

def index(request):
    return render(request, "fguess/index.html")

def create_room(request):

    if request.method == "POST":
        username = request.POST.get('user_name', '')
        unique_id = get_random_string(length=6)

        room = Room(name=unique_id, identifier=unique_id)

        room.save()

        user = CustomUser(username=username, is_admin=True, room=room)

        user.save()
        
        return redirect('room', unique_id)
    
def join_room(request):
    if request.method == "POST":
        username = request.POST.get('user_name', '')
        room_id = request.POST.get('room_id', '')

        try:
            room = Room.objects.get(identifier=room_id)
        except Room.DoesNotExist:
            room = None

        if (room == None):
            return redirect('index')
        else:
            user = CustomUser(username=username, is_admin=False, room=room)
            user.save()
            return redirect('room', room_id)
        

def room(request,number_room):

    room  = Room.objects.get(identifier=number_room)
    room_users = room.users.all()

    context = {
        'number_room': number_room,
        'room_users': room_users
    }
    return render(request, "fguess/room.html", context)