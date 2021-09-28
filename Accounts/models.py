from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

System = [
    ("دبلومة العلوم اللاهوتية", "دبلومة العلوم اللاهوتية"),
    ("بكالوريوس العلوم اللاهوتية", "بكالوريوس العلوم اللاهوتية"),
    ("كورسات متخصصة", "كورسات متخصصة"),
    ("دراسات عليا", "دراسات عليا"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    diocese = models.CharField(max_length=50)
    church = models.CharField(max_length=100)
    father_of_confession = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    phone = models.CharField(max_length=11)
    qualification = models.CharField(max_length=100)
    job = models.CharField(max_length=100, null=True, blank=True)
    system = models.CharField(max_length=100, choices=System)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)