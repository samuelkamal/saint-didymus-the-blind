from django.db import models

# Create your models here.


class News_and_Adv(models.Model):
    Img = models.ImageField(upload_to='media/', null=True, blank=True)
    Title = models.CharField(max_length=500)
    Description = models.TextField()

    def __str__(self):
        return self.Title