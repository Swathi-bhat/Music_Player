# urls.py

from django.urls import path
from .views import song_list, play_song, login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('song_list/', song_list, name='song_list'),
    path('song/<int:song_id>/', play_song, name='play_song'),
]
