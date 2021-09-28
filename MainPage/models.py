from django.db import models
from django.utils.text import slugify
# Create your models here.

class Main_Pic(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return 'main pic'

class Dar_El_Nashr(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'dar el nashr'

class Magazin(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'magazin'

class Library(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'library'

class Dibloma(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'diploma'

class Bachelor(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'bachelor'

class Specialized_Courses(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'specialized courses'

class Postgraduate(models.Model):
    Pic = models.ImageField(upload_to='media/', null=True, blank=True)
    Description = models.TextField()

    def __str__(self):
        return 'postgraduate'

class Who_We_Are(models.Model):
    Description = models.TextField()

    def __str__(self):
        return 'who we are'

class Follow_Us(models.Model):
    Title = models.CharField(max_length=15)
    Description = models.TextField()
    Link = models.CharField(max_length=1000)

    def __str__(self):
        return self.Title