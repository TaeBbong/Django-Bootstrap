from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='media', default='devkor_logo_mini.png')
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title

class AdPost(models.Model):
    CATEGORY_CHOICES = (
        ('Select Category', 'Select Category'), ('Portfolio', 'Portfolio'), ('Seminar', 'Seminar')
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.TextField(choices=CATEGORY_CHOICES, default='Select Category')
    created_date = models.DateTimeField(
        default=timezone.now)
    thumb = models.ImageField(upload_to='thumb', default='devkor_logo_mini.png')
    file = models.FileField(upload_to='file', default=None)

    def __str__(self):
        return self.title

class Images(models.Model):
    adpost = models.ForeignKey(AdPost, default=None)
    image = models.ImageField(upload_to='media', verbose_name='Image')

class Study(models.Model):
    leader = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    thumb = models.ImageField(upload_to='thumb', default='devkor_logo_mini.png')

    def __str__(self):
        return self.title
