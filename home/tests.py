# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class CommentView:
    def __init__(self):
        self.user = None
        self.content = ''
        self.date_publish = None
        self.thumbsup = 0


class ArticleView:
    def __init__(self):
        self.id = 0
        self.content = ''
        self.user = None
        self.date_publish = None
        self.thumbsup = 0
        self.comments = []
        self.comments_length

# Create your tests here.
class Ques_Article:
    def __init__(self):
        self.qid = 0
        self.tags = []
        self.queston_decs = ''
        self.queston_title = ''
        self.articles = []
        self.article_count = 0


class TestCase(TestCase):
    question = Question.objects.get(id=1)

    ques_art = Ques_Article()
    ques_art.qid = question.id
    ques_art.tags = question.tag.all()
    ques_art.queston_title = question.title
    ques_art.queston_decs = question.desc
    # ques_art.articles=question.article.all()
    count = Question.objects.filter(id=1).annotate(count=Count('article')).values('count')[0]
    ques_art.article_count = count['count']

    # print unicode(question.title),question.id
    # for t in question.tag.all():
    #     print unicode(t)

    ques_art.articles=[]

    articles = question.article.all()
    for art in articles:
        arti_view = ArticleView()
        arti_view.id=art.id
        arti_view.content=art.content
        arti_view.date_publish=art.date_publish
        arti_view.thumbsup=art.thumbsup
        arti_view.user=art.user

        arti_view.comments=[]

        for com in art.comment.all():
            #print unicode(c.content)
            com_view=CommentView()
            com_view.user=com.user
            com_view.content=com.content
            com_view.date_publish=com.date_publish
            com_view.thumbsup=com.thumbsup
            arti_view.comments.append(com_view)

        ques_art.articles.append(arti_view)



    print ques_art.qid,unicode(ques_art.queston_title),ques_art.article_count
    for t in ques_art.tags:
        print unicode(t)

    for q_art in ques_art.articles:
        print q_art.id,q_art.user.nickname,q_art.date_publish

        for comm in q_art.comments:
            print unicode(comm.content),unicode(comm.user.nickname)