from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.crypto import get_random_string
from fguess.models import Room, CustomUser, UploadedFile
from .forms import UploadForm

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
        
        return redirect('room', unique_id, user.id)
    
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
            return redirect('room', room_id, user.id)
        

def room(request,number_room, user_id):

    room  = Room.objects.get(identifier=number_room)
    room_users = room.users.all()

    
    user = CustomUser.objects.get(id=user_id)

    context = {
        'number_room': number_room,
        'room_users': room_users,
        'user': user,        
    }

    if (user.is_admin):
        return render(request, "fguess/room_admin.html", context)
    else:
        return render(request, "fguess/room.html", context)
    
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UploadForm()
    return render(request, 'fguess/upload.html', {'form': form})

def view_files(request,number_room):
    files = UploadedFile.objects.filter(room=number_room)
    return render(request, 'fguess/files.html', {'files': files})
#temporal