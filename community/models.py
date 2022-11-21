from django.db import models
from users.models import User

class Movie(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=50)
    image = models.ImageField()
    original_title = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return str(self.title)