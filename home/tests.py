# -*- coding: utf-8 -*-
from django.db.models import Max
from django.test import TestCase
from home.models import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import re

dr = re.compile(r'<[^>]+>', re.S)


# Create your tests here.
class Elem():
    pass

def page(question_list):
    index_content = []
    for question in question_list:
        elem = Elem()
        elem.question_id = question.id
        elem.question_title = question.title
        elem.date_publish = question.date_publish
        elem.question_tag = tag = question.tag.all()[:2]
        elem.focus_num = question.focus_num
        elem.article = question.article.annotate(Max('thumbsup'))[0]
        index_content.append(elem)
    return index_content

class TestCase(TestCase):

    question_list = Question.objects.all()
    index_content=page(question_list)
    for index in index_content:
        print index.question_title, index.date_publish, index.article.user.nickname
        for t in index.question_tag:
            print unicode(t)
