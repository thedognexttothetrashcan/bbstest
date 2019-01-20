from django.db import models

from user.models import User


class Post(models.Model):
    uid = models.IntegerField()
    title = models.CharField(max_length=64)
    create = models.DateTimeField(auto_now_add=True)
    updata = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-create']

    @property
    def auth(self):
        if not hasattr(self,'_auth'):
            self._auth = User.objects.get(pk=self.uid)
        return self._auth

    def comments(self):
        return Comment.objects.filter(post_id=self.id)

class Comment(models.Model):
    uid = models.IntegerField()
    post_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


    @property
    def post(self):
        if not hasattr(self,'_post'):
            self._post = Post.objects.get(pk=self.post_id)
        return self._post

    class Meta:
        ordering = ['-created']





