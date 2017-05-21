# -*- coding: utf-8 -*-
from models import Message, Question, Follow, Comment, User, Article, Tag

from django.db.models import Max, Count
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import datetime
import re
from django.db.models import Q

# 分页代码
def getPage(request, query_list):
    paginator = Paginator(query_list, 2)
    try:
        page = request.GET.get('num', 1)
        handle_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        handle_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        handle_list = paginator.page(paginator.num_pages)
    return handle_list


class Elem():
    def __init__(self):
        self.question_id = 0
        self.question_title = ''
        self.date_publish = ''
        self.likes = 0
        self.simple_desc = None


# def getSequence(length, divide):
#     seq = []
#     while (length > divide):
#         seq.append(divide)
#         length = length - divide
#     seq.append(length)
#
#     start = 0
#     result = []
#     for s in seq:
#         end = start + s
#         tup = (start, end)
#         start = end
#         result.append(tup)
#     return result


def getIndexPage(query):
    content = []
    for question in query:
        elem = Elem()
        elem.question_id = question.id
        elem.question_title = question.title
        elem.date_publish = question.date_publish
        elem.likes = question.likes
        article = question.article.annotate(Max('thumbsup'))[0]
        if article:
            elem.article = article
            dr = re.compile(r'<[^>]+>', re.S)
            dd = dr.sub('', article.content)
            elem.simple_desc = dd
        content.append(elem)
    return content


# def showPage(query, result, pagenum):
#     start = result[pagenum][0]
#     end = result[pagenum][1]
#     query = query[start:end]
#     index_content = getIndexPage(query)
#     return index_content


class MostReply:
    def __init__(self):
        self.id = 0
        self.count = 0
        self.title = ''


def getMostReply(query):
    MostReply_list = []
    for q in query:
        reply = MostReply()
        reply.count = q['count']
        reply.title = unicode(q['title'])
        reply.id = q['id']
        MostReply_list.append(reply)

    return MostReply_list


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
        self.comments_length = 0


def similarQues(tags):
    string = ''
    for t in tags:
        string = string + 'Q(tag__name__contains=' + '"' + unicode(t) + '"' + ')|'
    string = string[:-1]
    #print string
    string = 'Question.objects.filter(' + string + ')' + '.order_by("-likes").distinct()[:5]'
    similarQ = eval(string)
    return similarQ


class Ques_Article:
    def __init__(self):
        self.qid = 0
        self.tags = []
        self.queston_author = None
        self.likes = 0
        self.queston_decs = ''
        self.queston_title = ''
        self.articles = []
        self.article_count = 0
        self.similarQ = []


def getArticleCommet(qid):
    question = Question.objects.get(id=qid)
    ques_art = Ques_Article()
    ques_art.qid = question.id
    ques_art.tags = question.tag.all()
    ques_art.queston_author = question.author
    ques_art.queston_title = question.title
    ques_art.likes = question.likes
    ques_art.queston_decs = question.desc
    ques_art.similarQ = similarQues(ques_art.tags)
    count = Question.objects.filter(id=qid).annotate(count=Count('article')).values('count')[0]
    ques_art.article_count = count['count']
    ques_art.articles = []
    articles = question.article.all().order_by('-thumbsup')
    for art in articles:
        arti_view = ArticleView()
        arti_view.id = art.id

        arti_view.content = art.content
        arti_view.date_publish = art.date_publish
        arti_view.thumbsup = art.thumbsup
        arti_view.user = art.user

        arti_view.comments = []

        for com in art.comment.all():
            com_view = CommentView()
            com_view.user = com.user
            com_view.content = com.content
            com_view.date_publish = com.date_publish
            com_view.thumbsup = com.thumbsup
            arti_view.comments.append(com_view)
        arti_view.comments_length = len(arti_view.comments)
        ques_art.articles.append(arti_view)
    return ques_art


def getFollowId(uid):
    id_list = Follow.objects.filter(follower_id=uid).values_list('followee_id')
    follow_list = []
    for id in id_list:
        follow_list.append(id[0])
    return follow_list


def saveComment(uid, content, aid):
    user = User.objects.get(id=uid)
    comment = Comment()
    comment.user = user
    now = datetime.datetime.now()
    comment.date_publish = now
    comment.content = content
    comment.save()
    article = Article.objects.get(id=aid)
    article.comment.add(comment)


def sendMessage(from_id, to_id, content):
    message = Message()
    message.from_user_id = from_id
    message.to_user_id = to_id
    message.content = content
    message.date_publish = datetime.datetime.now()
    message.save()


class Profile:
    def __init__(self):
        self.user = None
        self.questions = []  # 提问
        self.answers = []  # 回答
        self.following_list = []
        self.following_count = 0
        self.followed_list = []
        self.followed_count = 0


def getProfile(uid):
    pro = Profile()
    u = User.objects.get(id=uid)
    pro.user = u
    pro.questions = Question.objects.filter(author=u).order_by('date_publish')

    arti = Article.objects.filter(user=u)
    answers = Question.objects.filter(article=arti).order_by('date_publish')
    pro.answers = answers

    foing_list = []
    followee_ids = Follow.objects.filter(follower_id=uid).values_list('followee_id')
    for ids in followee_ids:
        user = User.objects.get(id=ids[0])
        foing_list.append(user)
    pro.following_list = foing_list
    pro.following_count = len(foing_list)

    foed_list = []
    follower_ids = Follow.objects.filter(followee_id=uid).values_list('follower_id')
    for ids in follower_ids:
        user = User.objects.get(id=ids[0])
        foed_list.append(user)
    pro.followed_list = foed_list
    pro.followed_count = len(foed_list)
    return pro


def askQuestion(uid, title, desc, tags):
    #print uid,title,desc,tags
    #ques, created = Question.objects.get_or_create(title=title)
    QList=Question.objects.filter(title=title)
    #print created
    print QList
    #if QList :
    print 'hello'
    ques=Question()
    ques.title = title
    ques.desc = desc
    ques.likes = 0
    ques.date_publish = datetime.datetime.now()
    print ques.date_publish
    u = User.objects.get(id=uid)
    ques.author = u

    ques.save()
    print ques
    for tag in tags:
        if tag:
            t, created = Tag.objects.get_or_create(name=tag)
            ques.tag.add(t)


def saveArticle(uid, qid, content):
    question = Question.objects.get(id=qid)
    article = question.article.filter(user_id=uid)
    print article
    if article:
        for art in article:
            art.content = content
            art.save()
    else:
        art = Article()
        u = User.objects.get(id=uid)
        art.user = u
        art.content = content
        art.date_publish = datetime.datetime.now()
        art.save()
        question.article.add(art)
