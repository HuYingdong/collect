from django.db import models


class Bookmark(models.Model):
    issue = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    sort = models.CharField(max_length=20, default='unknown')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='bookmarks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookmark'
        ordering = ('sort',)

    def __str__(self):
        return self.issue


class Command(models.Model):
    issue = models.CharField(max_length=255)
    cmd = models.CharField(max_length=255, unique=True)
    remark = models.CharField(max_length=255, default='null')
    sort = models.CharField(max_length=20, default='unknown')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='commands', on_delete=models.CASCADE)

    class Meta:
        db_table = 'command'
        ordering = ('sort',)

    def __str__(self):
        return self.issue


class UserInfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )

    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'userinfo'


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    # 时间限制
    # 次数限制

    class Meta:
        db_table = 'usertoken'
