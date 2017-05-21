# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from handle import askQuestion


class TestCase(TestCase):
    uid=2
    titl='关于时间有哪些细思恐极的细节？'
    desc='欢迎邀请回答，谢谢。'
    tags=['时间','物理学','宇宙','脑洞','X 有哪些细思恐极的细节']
    askQuestion(uid=2,title=titl,desc=desc,tags=tags)
