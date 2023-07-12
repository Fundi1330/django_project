from django.db import models
from .base import Base
from .post import Post

class Comment(Base):
    body = models.CharField(max_length=1200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)