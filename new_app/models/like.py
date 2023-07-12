from django.db import models
from .base import Base
from .post import Post


class Like(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)