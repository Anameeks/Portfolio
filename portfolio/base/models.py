from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True, null=True)  # FontAwesome icon name

    def __str__(self):
        return self.platform


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Hobby(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
