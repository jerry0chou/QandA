# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import AbstractUser


# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(AbstractUser):
    nickname = models.CharField(max_length=50, default='', verbose_name='昵称')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    sex = models.BooleanField('性别', max_length=2, choices=((0, '男'), (1, '女'),), default=0)
    self_description = models.CharField('描述', max_length=256, default='我什么都没写')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Follow(models.Model):
    followee = models.ForeignKey(User, verbose_name='被关注人')

    class Meta:
        verbose_name = '关注人'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return str(self.id)


# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30,unique=True, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    content = models.TextField(verbose_name='文章内容')
    thumbsup = models.IntegerField(default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')

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
    focus_num = models.IntegerField(default=0, verbose_name='关注量')
    article = models.ForeignKey(Article,blank=True, null=True, verbose_name='文章')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='评论用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='所属文章')
    thumbsup = models.IntegerField(default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)


class Message(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='消息用户')
    content = models.TextField(verbose_name='信息内容', blank=True, null=True)
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间', blank=True, null=True)

    class Meta:
        verbose_name = '消息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)
