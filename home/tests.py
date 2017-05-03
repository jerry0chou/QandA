# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re

dr = re.compile(r'<[^>]+>', re.S)


# Create your tests here.
class MostReply:
    def __init__(self):
        self.id=0
        self.count=0
        self.title=''

class TestCase(TestCase):
    question_list=Question.objects.annotate(count=Count('article')).values('count','title','id').order_by('-count')[:3]

    reply_list=[]
    for q in question_list:
        reply = MostReply()
        reply.count=q['count']
        reply.title=unicode(q['title'])
        reply.id=q['id']
        reply_list.append(reply)

    for reply in reply_list:
        print reply.count,reply.title,reply.id

