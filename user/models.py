from django.db import models

class User(models.Model):
    SEX = (
        ('M','男性'),
        ('F','女性'),
        ('S','保密'),
    )
    nickname = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=8,choices=SEX)
    icon = models.ImageField()
    # 关联权限表prem_id
    # prem_id = models.IntegerField()

    def roles(self):
        '''当前用户具有的所有角色'''
        relations = UserRoleRelation.objects.filter(uid=self.id).only('role_id')
        role_id_list = [r.role_id for r in relations]

        return Role.objects.filter(id__in=role_id_list)

    def has_prem(self, perm_name):
        # need_perm = Permission.objects.get(name=perm_name)
        # self_perm = Permission.objects.get(pk=self.prem_id)
        # return self_perm.level >= need_perm.level
        for role in self.roles():
            for perm in role.perm():
                if perm == perm_name:
                    return True
        return False


class UserRoleRelation(models.Model):
    uid = models.IntegerField()
    role_id = models.IntegerField()

    @classmethod
    def add_role_for_user(cls, uid, role_id):
        cls.objects.create(uid=uid, role_id=role_id)

    @classmethod
    def del_role_from_user(cls,uid,role_id):
        cls.objects.get(uid=uid,role_id=role_id).delete()

class Role(models.Model):
    '''
    角色表
        admin
        manager
        user
    '''
    name = models.CharField(max_length=32)

    def perm(self):
        '''当前角色具有的所有权限'''
        relations = RolePerRelation.objects.filter(role_id=self.id).only('perm_id')
        perm_id = [r.perm_id for r in relations]
        return Permission.objects.filter(id__in=perm_id)


class RolePerRelation(models.Model):
    role_id = models.IntegerField()
    perm_id = models.IntegerField()

    @classmethod
    def add_perm_for_role(cls,role_id,perm_id):
        cls.objects.create(role_id=role_id, perm_id=perm_id)

    @classmethod
    def del_perm_from_role(cls, role_id,perm_id):
        cls.objects.get(role_id=role_id,perm_id=perm_id).delete()

class Permission(models.Model):
    '''
    权限表
        add_post    添加帖子
        add_comment 添加评论
        add_manager
        del_post
        del_comment
        del_manager
        del_user
    '''
    name = models.CharField(max_length=32)
    # level = models.IntegerField()










