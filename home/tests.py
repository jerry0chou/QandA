# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from models import *
from django.db.models import Q
import datetime



class TestCase(TestCase):
    question = Question.objects.get(id=3)
    article = question.article.filter(user_id=15)[:1]
    if article:
        article.content = "我来测试保存文章 一堆多"
        article.save()
    else:
        art = Article()

        article.content = "我来测试保存文章 一堆多"
        art.date_publish = datetime.datetime.now()
        art.save()
        question.article.add(art)
