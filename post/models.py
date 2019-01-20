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










