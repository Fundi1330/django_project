from django.db import models
from .base import Base

class Post(Base):
    body = models.TextField()
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='./', default='/media/images/default.png')
    # likes = models.ManyToManyField()