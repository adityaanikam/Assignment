from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    # List of available chat rooms
    path('', views.room_list, name='room_list'),

    # A shared room for all users
    path('chat/common/', views.chat_room, {'room_name': 'common'}, name='common_room'),

    # Dynamic room name based on a string
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),

    # Room based on an integer ID (optional)
    path('chat/id/<int:room_id>/', views.chat_room_by_id, name='chat_room_by_id'),
]
