from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Add more author details if needed

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Add other fields for the post if needed

    def __str__(self):
        return self.title

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True)
    # You can add more fields specific to images if needed

class Video(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post_videos/',blank=True)
    # You can add more fields specific to videos if needed

class PDF(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='post_pdfs/',blank=True)
    # You can add more fields specific to PDFs if needed