# -*- coding: utf-8 -*-
import json

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from handle import  getMostReply, getArticleCommet, saveComment, sendMessage, getFollowId, \
    getProfile, askQuestion, saveArticle,getPage,getIndexPage
from home.models import User, Follow, Message, Question
from home.verify import verify_username, verify_phone, verify_pwd, verify_pwd2, verify_email
from django.db.models import Q
import re

def global_setting(request):
    client = request.session.get('client', default=None)
    searchStr=request.session.get('searchStr', default='')
    NewQues = Question.objects.all().order_by('-date_publish')[:3]
    MostLikes = Question.objects.all().order_by('-likes')[:3]
    question_list = Question.objects.annotate(count=Count('article')).values('count', 'title', 'id').order_by('-count')[
                    :3]
    if client:
        followId_list = getFollowId(client.id)
    MostReply = getMostReply(question_list)
    return locals()


@csrf_exempt
def index(request):
    searchText=request.GET.get('searchText', default='')
    print searchText,':SEARCH'
    request.session['searchStr'] = searchText

    if searchText:
        Qlist= Question.objects.filter(Q(title__contains=searchText)|Q(tag__name__contains=searchText)).distinct().order_by('-likes')
    else:
        Qlist = Question.objects.all().order_by('-likes')

    query=getPage(request,Qlist)
    index_content=getIndexPage(query)
    return render(request, 'index.html', locals())

@csrf_exempt
def login_reg(request):
    if request.method == 'POST':
        if len(request.POST) == 2:
            name = request.POST['username']
            pwd = request.POST['password']
            user_set = User.objects.filter(username=name, password=pwd)
            client = User()
            for u in user_set:
                client = u
            if client.username:
                request.session['client'] = client
                return HttpResponse('ok')
            else:
                return HttpResponse('用户名或密码输入错误')

        elif len(request.POST) == 6:
            name = request.POST['username']
            nickname = request.POST['nickname']
            phone = request.POST['mobile']
            pwd = request.POST['password']
            pwd2 = request.POST['password2']
            sex = request.POST['sex']
            name_dic = verify_username(name)
            phone_dic = verify_phone(phone)
            pwd_dic = verify_pwd(pwd, pwd2)
            dictMerged = dict(name_dic.items() +
                              phone_dic.items() + pwd_dic.items())
            if dictMerged['phone'] == '' and dictMerged['name'] == '' and dictMerged['pwd'] == '':
                user = User()
                user.username = name
                user.nickname = nickname
                user.mobile = phone
                user.password = pwd
                user.sex = sex
                user.save()
            return HttpResponse(json.dumps(dictMerged))
    else:
        return render(request, 'login_reg.html', locals())


@csrf_exempt
def logout(request):
    client = request.session.get('client', default=None)
    if client:
        del request.session['client']
        return HttpResponse('ok')
    else:
        return HttpResponse('please login')


@csrf_exempt
def article(request):
    followerId = request.GET.get('follower_id')
    followeeIid = request.GET.get('followee_id')
    followTip = request.GET.get('follow_tip')
    qid = request.GET.get('qid')

    user_id = request.GET.get('user_id')
    comment_text = request.GET.get('comment_text')
    article_id = request.GET.get('article_id')

    from_user_id = request.GET.get('from_user_id')
    to_user_id = request.GET.get('to_user_id')
    message_text = request.GET.get('message_text')

    if followerId and followeeIid:
        if followTip == 'cancel':
            foll = Follow.objects.get(follower_id=int(
                followerId), followee_id=followeeIid)
            foll.delete()
            return HttpResponse('canceled')
        elif followTip == 'ok':
            foll = Follow(follower_id=int(followerId), followee_id=followeeIid)
            foll.save()
            return HttpResponse('focused')

    elif qid:
        ques_article = getArticleCommet(int(qid))
        return render(request, 'article_detail.html', locals())

    elif user_id and comment_text and article_id:
        saveComment(uid=user_id, content=comment_text, aid=article_id)
        return HttpResponse('ok')

    elif from_user_id and to_user_id and message_text:
        sendMessage(from_id=from_user_id,
                    to_id=to_user_id, content=message_text)
        return HttpResponse('ok')


@csrf_exempt
def profile(request):
    uid = request.GET.get('uid')
    sex = request.GET.get('sex')
    self_description = request.GET.get('self_description')
    mobile = request.GET.get('mobile')
    email = request.GET.get('email')
    oldPwd = request.GET.get('oldPwd')
    newPwd = request.GET.get('newPwd')
    # print sex, self_description, mobile, oldPwd, newPwd

    client = request.session.get('client', default=None)

    if uid:
        profile = getProfile(uid)
        return render(request, 'profile.html', locals())
    elif sex and self_description and mobile and email and oldPwd and newPwd:
        print sex, self_description, email, mobile, oldPwd, newPwd
        phone_list = verify_phone(mobile)
        user = User.objects.get(id=client.id)
        print '------', unicode(phone_list['phone']), user.password, verify_email(email), verify_pwd2(newPwd)
        if phone_list['phone'] == '' and user.password == oldPwd and verify_email(email) == 'ok' and verify_pwd2(
                newPwd) == 'ok':
            print user.username, 'testests'
            # user.sex=sex
            # user.self_description=self_description
            # user.mobile=mobile
            # user.email=email
            # user.password=newPwd
            # user.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('error')


@csrf_exempt
def inbox(request):
    client = request.session.get('client', default=None)

    from_id = request.GET.get('from_id')
    to_id = request.GET.get('to_id')
    m_text = request.GET.get('m_text')
    print type(from_id), type(m_text)
    if from_id and to_id and m_text:
        print from_id, to_id, m_text, 'inside'
        sendMessage(from_id=from_id, to_id=to_id, content=m_text)
        return HttpResponse('ok')

    elif client:
        message_list = Message.objects.filter(Q(from_user=client.id) | Q(
            to_user=client.id)).order_by('-date_publish')
        return render(request, 'inbox.html', locals())


@csrf_exempt
def ask(request):
    if request.method == 'POST':
        client = request.session.get('client', default=None)
        if client:
            q_name = request.POST['question_name']
            q_desc = request.POST['question_description']
            q_tag = request.POST['question_tag']
            q_tags = re.split(' |,|\.|;|\*|\n', q_tag)
            print q_name,q_desc,q_tag
            askQuestion(uid=client.id, title=q_name, desc=q_desc, tags=q_tags)
            return HttpResponse('ok')


@csrf_exempt
def answer(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        question_id = request.POST['question_id']
        article_content = request.POST['article_content']
        saveArticle(uid=user_id, qid=question_id, content=article_content)
        return HttpResponse('ok')
    else:
        qid = request.GET.get('qid')
        client = request.session.get('client', default=None)
        if qid and client:
            question = Question.objects.get(id=qid)
            tags = question.tag.all()
            article = question.article.filter(user_id=client.id)
        return render(request, 'answer.html', locals())

