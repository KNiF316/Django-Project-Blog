from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    createdDate = models.DateField()
    author = models.CharField(max_length=20)
    description = models.TextField()
    isPublished = models.CharField(max_length=10)