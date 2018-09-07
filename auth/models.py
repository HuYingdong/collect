from django.db import models


class UserInfo(models.Model):
    user_type_choices = (
        (1, '只读'),
        (2, '读写改'),
        (3, '读删'),
        (4, '读写改删')
    )

    user_type = models.IntegerField(choices=user_type_choices, default=1)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user_info'


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo')
    token = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    # 时间限制
    # 次数限制

    class Meta:
        db_table = 'user_token'
