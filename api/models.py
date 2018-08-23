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


class Note(models.Model):
    issue = models.CharField(max_length=255)
    cmd = models.CharField(max_length=255)
    remark = models.CharField(max_length=255, default='null')
    sort = models.CharField(max_length=20, default='unknown')
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'note'
        ordering = ('sort',)

    def __str__(self):
        return self.issue
