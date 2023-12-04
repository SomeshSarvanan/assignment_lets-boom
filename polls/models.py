from django.db import models

# Create your models here.
class books(models.Model):
    BookTitle = models.CharField(max_length=255)
    BookAuthor = models.CharField(max_length=255)
    BookId = models.IntegerField()
