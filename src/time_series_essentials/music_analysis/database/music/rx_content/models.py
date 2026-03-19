from django.db import models

# Create your models here.

class Track(models.Model):
    artist = models.CharField(max_length = 1000, null = True)
    name = models.CharField(max_length = 1000, null = True)
    album = models.CharField(max_length = 1000, null = True)
    composer = models.CharField(max_length = 1000, null = True)
    genre = models.CharField(max_length = 1000, null = True)
    average_bpm = models.FloatField(null = True)
    tonality = models.CharField(max_length = 10, null = True)
    energy = models.IntegerField(null = True)
    total_time = models.IntegerField(null = True)
    dynamic = models.BooleanField(null = True)
    year = models.IntegerField(null = True)
    rekordbox_track_id = models.IntegerField(db_index=True)
    
    # This is the only field that requires content
    location = models.CharField(max_length = 1000)
