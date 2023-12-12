from django.db import models
from core.models import TimestampZone


class Post(TimestampZone):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(TimestampZone):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
