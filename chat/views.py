from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ChatRoom, Message
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})


def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})

@login_required
def room_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/room_list.html', {'users': users})


@login_required
def chat_room_by_id(request, room_id):
    other_user = User.objects.get(id=room_id)
    users = User.objects.exclude(id=request.user.id)
    context = {
        'room_id': str(room_id),
        'other_user': other_user,
        'users': users,
    }
    return render(request, 'chat/chat_room.html', context)
