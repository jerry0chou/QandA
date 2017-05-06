# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *

# Create your tests here.

import datetime


class Profile:
    def __init__(self):
        self.user=None
        self.questions=[] #提问
        self.answers=[]  # 回答
        self.following_list=[]
        self.following_count=0
        self.followed_list=[]
        self.followed_count=0

class TestCase(TestCase):

    pro=Profile()
    u=User.objects.get(id=2)
    pro.user=u
    pro.questions=Question.objects.filter(author=u)

    arti = Article.objects.filter(user=u)
    answers = Question.objects.filter(article=arti)
    pro.answers=answers

    foing_list=[]
    followee_ids=Follow.objects.filter(follower_id=2).values_list('followee_id')
    for ids in followee_ids:
        user=User.objects.get(id=ids[0])
        foing_list.append(user)
    pro.following_list=foing_list
    pro.following_count=len(foing_list)

    foed_list=[]
    follower_ids=Follow.objects.filter(followee_id=2).values_list('follower_id')
    for ids in follower_ids:
        user=User.objects.get(id=ids[0])
        foed_list.append(user)
    pro.followed_list=foed_list
    pro.followed_count=len(foed_list)