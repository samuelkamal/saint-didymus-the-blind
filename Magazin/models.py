from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.


class Carousel(models.Model):
    Img_1 = models.ImageField(upload_to = 'media/')
    Title_1 = models.CharField(max_length=200)
    Description_1 = models.TextField()

    Img_2 = models.ImageField(upload_to = 'media/')
    Title_2 = models.CharField(max_length=200)
    Description_2 = models.TextField()

    Img_3 = models.ImageField(upload_to = 'media/')
    Title_3 = models.CharField(max_length=200)
    Description_3 = models.TextField()

    def __str__(self):
        return 'Carousel'


class Magazin_Number(models.Model):
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    DownLoad_Link = models.CharField(max_length=1000)

    def __str__(self):
        return self.Title