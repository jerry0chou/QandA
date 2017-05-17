# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from models import *
from django.db.models import Q
import datetime



class TestCase(TestCase):
    # tags=['社会','电影','政治']
    # string=''
    # for t in tags:
    #     string=string+'Q(tag__name__contains='+'"'+unicode(t)+'"'+')|'
    # string=string[:-1]
    # print string
    # string='Question.objects.filter('+string+')'+'.order_by("-likes")[:5]'
    # print string
    # Qlist=eval(string)
    # for q in Qlist:
    #     print unicode(q.title)
    Qlist=Question.objects.filter(Q(tag__name__contains="穿衣") | Q(tag__name__contains="打扮") | Q(tag__name__contains="时尚") | Q(tag__name__contains="生活") | Q(tag__name__contains="男装") | Q(tag__name__contains="服饰搭配")).order_by("-likes").distinct()
    for q in Qlist:
        print unicode(q.title)