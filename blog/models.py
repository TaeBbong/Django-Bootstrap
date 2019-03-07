from django.db import models
from django.utils import timezone
from easy_thumbnails import fields


class Post(models.Model): # Announcement
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = fields.ThumbnailerImageField(
        upload_to='thumb',
        default='devkor_logo_mini.png',
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    file = models.FileField(upload_to='file', default=None)

    def __str__(self):
        return self.title

class Portfolio(models.Model): # Portfolio
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = fields.ThumbnailerImageField(
        upload_to='thumb',
        default='devkor_logo_mini.png',
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    file = models.FileField(upload_to='file', default=None)

    def __str__(self):
        return self.title

class Activity(models.Model): # Activity
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = fields.ThumbnailerImageField(
        upload_to='thumb',
        default='devkor_logo_mini.png',
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    file = models.FileField(upload_to='file', default=None)

    def __str__(self):
        return self.title

class Seminar(models.Model): # Seminar
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumbnail = fields.ThumbnailerImageField(
        upload_to='thumb',
        default='devkor_logo_mini.png',
    )
    created_date = models.DateTimeField(
            default=timezone.now)
    file = models.FileField(upload_to='file', default=None)

    def __str__(self):
        return self.title


class Study(models.Model):
    leader = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumb = models.ImageField(upload_to='thumb', default='devkor_logo_mini.png')

    def __str__(self):
        return self.title
