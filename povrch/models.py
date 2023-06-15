from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class PictureDb(models.Model):
    name = models.CharField(max_length=100)
    webpage = models.URLField()
    picture1 = models.ImageField(upload_to='images/')
    picture2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
