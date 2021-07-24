from django.db import models
from posts.models import Post

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='tags')

    def __str__(self):
        return self.title
