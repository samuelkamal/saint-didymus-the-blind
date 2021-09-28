from django.db import models
from django.utils.text import slugify

# Create your models here.


class Categories(models.Model):
    Title = models.CharField(max_length=200)
    Slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title, allow_unicode=True)
        super(Categories, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title


class Add_Book(models.Model):
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Img = models.ImageField(upload_to='media/')
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    Link = models.CharField(max_length=1000)
    Slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title, allow_unicode=True)
        super(Add_Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.Title


class Advertisement(models.Model):
    Adv = models.CharField(max_length=3000)

    def __str__(self):
        return self.Adv