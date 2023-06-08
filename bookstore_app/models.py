from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    # Other fields...

    def __str__(self):
        return self.title
