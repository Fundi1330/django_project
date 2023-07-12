from .base import Base
from django.db import models
from django.contrib.auth.models import User

class Profile(Base):
    username = models.CharField(max_length=140)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='./images/', default='/media/images/avatars/default.png')
    bio = models.TextField()