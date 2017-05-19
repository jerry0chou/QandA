# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import AbstractUser
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')


# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息


class User(AbstractUser):
    profile=models.TextField('头像',default='<img width="300" class="img-responsive img-thumbnail" src="/uploads/default/zhi.jpg" />')
    nickname = models.CharField(max_length=50, default='', verbose_name='昵称')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    sex = models.BooleanField('性别', max_length=2, choices=((0, '男'), (1, '女'),), default=0)
    self_description = models.CharField('描述', max_length=256, default='我什么都没写')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        if self.nickname is not None:
            return self.nickname
        else:
            return self.username


class Follow(models.Model):
    follower = models.ForeignKey(User, blank=True, null=True, related_name='follower_id', verbose_name='关注人')
    followee = models.ForeignKey(User, blank=True, null=True, related_name='followee_id', verbose_name='被关注人')

    class Meta:
        verbose_name = '关注'
        verbose_name_plural = verbose_name
        ordering = ['-id']
        unique_together = (("follower", "followee"),)

    def __unicode__(self):
        return str(self.id)


class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user_id', blank=True, null=True, verbose_name='发信人')
    to_user = models.ForeignKey(User, related_name='to_user_id', blank=True, null=True, verbose_name='收信人')
    content = models.TextField(verbose_name='私信内容', blank=True, null=True)
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间', blank=True, null=True)

    class Meta:
        verbose_name = '私信'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)


# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='评论用户')
    thumbsup = models.IntegerField(default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return 'id:'+str(self.id)+' '+self.user.nickname


class Article(models.Model):
    content = models.TextField(verbose_name='文章内容')
    thumbsup = models.IntegerField(default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='作者')
    comment = models.ManyToManyField(Comment, blank=True, null=True, verbose_name='评论')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name='问题名')
    desc = models.TextField(max_length=256, verbose_name='文章描述')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')
    likes = models.IntegerField(default=0, verbose_name='喜欢')
    article = models.ManyToManyField(Article, blank=True, null=True, verbose_name='文章')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    author=models.ForeignKey(User,blank=True, null=True, verbose_name='作者')

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title
