from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    album_art_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
