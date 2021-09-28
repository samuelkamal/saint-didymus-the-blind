from django.db import models
from django.utils.text import slugify

# Create your models here.

class Subject(models.Model):
    Title = models.CharField(max_length=150)
    Pic = models.ImageField(upload_to='media/')
    Test = models.CharField(max_length=300, null=True, blank=True)
    Slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title, allow_unicode=True)
        super(Subject, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title

class Lecture(models.Model):
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Title = models.CharField(max_length=150)
    Video = models.CharField(max_length=300)
    More_Info = models.TextField()
    Audio_Lecture = models.CharField(max_length=300, null=True, blank=True)
    Lecture_Files = models.CharField(max_length=300, null=True, blank=True)
    Sheet = models.CharField(max_length=300, null=True, blank=True)
    Test = models.CharField(max_length=300, null=True, blank=True)
    Slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title, allow_unicode=True)
        super(Lecture, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title


class Ads(models.Model):
    Ad = models.TextField()

    def __str__(self):
        return self.Ad