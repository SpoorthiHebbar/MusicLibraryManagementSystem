from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class artists(models.Model):
    artist_name = models.CharField(max_length=60)
    artist_image = models.ImageField(upload_to = 'pics')

class albums(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.ForeignKey(artists,on_delete = models.CASCADE)
    album_image = models.ImageField(upload_to='pics')
    genre = models.CharField(max_length=60)
    release_date = models.DateField()
    fave = models.BooleanField(default=False)

class tracks(models.Model):
    album = models.ForeignKey(albums,on_delete = models.CASCADE)
    track_title = models.CharField(max_length=200)
    track_length = models.CharField(max_length=60)

class list(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    track_id = models.ForeignKey(tracks,on_delete = models.CASCADE)




    



