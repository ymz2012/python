from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bbs(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True,null=True)
    content = models.TextField()
    auther = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
class BBS_user(models.Model):
    