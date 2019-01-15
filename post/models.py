from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)
    updata = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-create']
