import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class ProfilePhoto(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to='user_photo/')

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.photo.storage.delete(self.photo.name)
        super().delete()

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    user_photo = models.OneToOneField('ProfilePhoto', null=True, blank=True, on_delete=models.SET_NULL)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL, related_name="leads")
    category = models.ForeignKey('Category', related_name='leads', null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    added = models.DateField(auto_now=True)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='leads_photo/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    agent_photo = models.ImageField(null=True, blank=True, upload_to='agents_photo/')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)