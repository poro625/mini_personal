from django.db import models

class Movie(models.Model):

    movie_id = models.CharField(max_length=50)
    image = models.ImageField()
    original_title = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
