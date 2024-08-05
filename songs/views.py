from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Song

@login_required
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', {'songs': songs})

@login_required
def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    songs = Song.objects.all()  
    song_list = list(songs)  

    current_index = song_list.index(song)
    next_song = song_list[(current_index + 1) % len(song_list)]  # Loop back to the first song if at the end
    previous_song = song_list[(current_index - 1) % len(song_list)]  # Loop back to the last song if at the beginning

    return render(request, 'play_song.html', {
        'song': song,
        'next_song': next_song,
        'previous_song': previous_song
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('song_list')  # Redirect to song list or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
