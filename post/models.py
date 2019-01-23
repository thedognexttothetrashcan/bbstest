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
        if not hasattr(self, '_auth'):
            self._auth = User.objects.get(pk=self.uid)
        return self._auth

    def comments(self):
        return Comment.objects.filter(post_id=self.id)

    def tags(self):
        relations = PostTagRelation.objects.filter(post_id=self.id).only('tag_id')
        tag_id_list = [r.tag_id for r in relations]
        return Tag.objects.filter(id__in=tag_id_list)

    def update_tags(self, tag_names):
        exist_tags = set(self.tags())
        updated_tags = set(Tag.ensure_tags(tag_names))

        # 处理新增关系
        new_tags = updated_tags - exist_tags
        need_create_tid_list = [t.id for t in new_tags]
        PostTagRelation.add_relations(self.id, need_create_tid_list)

        # 处理需要删除的的关系
        old_tags = exist_tags - updated_tags
        need_del_tid_list = [t.id for t in old_tags]
        PostTagRelation.del_relations(self.id, need_del_tid_list)

class Comment(models.Model):
    uid = models.IntegerField()
    post_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    @property
    def post(self):
        if not hasattr(self, '_post'):
            self._post = Post.objects.get(pk=self.post_id)
        return self._post

    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    @classmethod
    def ensure_tags(cls, tag_name):
        # 过滤出已经存在的tag name
        exist_tags = cls.objects.filter(name__in=tag_name)
        exists_names = {t.name for t in exist_tags}

        # 创建不存在的 Tag
        not_exist_names = set(tag_name) - exists_names
        need_create_tags = [Tag(name=name) for name in not_exist_names]
        cls.objects.bulk_create(need_create_tags)
        return cls.objects.filter(name__in=tag_name)


class PostTagRelation(models.Model):
    '''
    帖子 - 标签 的关系
    '''
    post_id = models.IntegerField()
    tag_id = models.IntegerField()

    @classmethod
    def add_relations(cls, post_id, tag_id_list):
        need_create = [cls(post_id=post_id, tag_id=tid)
                       for tid in tag_id_list]
        cls.objects.bulk_create(need_create)

    @classmethod
    def del_relations(cls, post_id, tag_id_list):
        cls.objects.filter(post_id=post_id, tag_id__in=tag_id_list).delete()
