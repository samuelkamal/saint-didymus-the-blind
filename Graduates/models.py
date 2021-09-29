from django.db import models
from django.utils.text import slugify

# Create your models here.

class Year(models.Model):
    Title = models.CharField(max_length=30)
    Slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title, allow_unicode=True)
        super(Year, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title


class Students(models.Model):
    Year = models.ForeignKey(Year, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Certificate = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.Name