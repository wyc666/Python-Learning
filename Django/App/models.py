# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as Django_User

# Create your models here.
class BBS(models.Model):
    # 帖子标题
    title = models.CharField(max_length=64)
    # 帖子概要
    summary = models.CharField(max_length=256, blank=True, null=True)
    # 帖子内容
    content = models.TextField()
    # 帖子作者
    author = models.ForeignKey('User')
    # 属于的版块
    category = models.ForeignKey('Category')
    # 帖子浏览量
    view_count = models.IntegerField()
    # 帖子排名
    ranking = models.IntegerField()
    # 帖子创建时间
    created_at = models.DateTimeField()
    # 帖子更新时间
    updated_at = models.DateTimeField()

    # 默认返回的是帖子的title
    def __unicode__(self):
        return self.title

class Category(models.Model):
    # 板块名字
    name = models.CharField(max_length=64, unique=True)
    # 版主
    administrator = models.ForeignKey('User')

    # 默认返回的是帖子的name
    def __unicode__(self):
        return self.name

class User(models.Model):
    # 一对一的关联Django自带的User表
    user = models.OneToOneField(Django_User)
    # 用户的签名
    signature = models.CharField(max_length=128, default='This guy is too lazy to leave anything.')
    # 用户头像
    avator = models.ImageField(upload_to='avator_imgs/', default='avator_imgs/default_avator.jpg')

    #
    def __unicode__(self):
        return self.user.username
