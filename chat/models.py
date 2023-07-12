from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Chat(Base):
    name = models.CharField(max_length=80)
    avatar = models.ImageField(upload_to='./media', default='/media/default.png')
    members = models.ManyToManyField(User, related_name='members')
    

class Message(Base):
    body = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    replay_to = models.IntegerField(null=True)
    is_pinned = models.BooleanField(default=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

