# -*- coding: utf-8 -*-
from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from home.models import User, Article, Message, Question
from home.verify import verify_username, verify_phone, verify_pwd
import json
import re

dr = re.compile(r'<[^>]+>', re.S)


class Elem():
    def __init__(self):
        self.question_id = 0
        self.question_title = ''
        self.date_publish = ''
        self.question_tag = None
        self.focus_num = 0
        self.simple_desc = None


def global_setting(request):
    client = request.session.get('client', default=None)

    index_content = []
    question_list = Question.objects.all()
    for question in question_list:
        elem = Elem()
        elem.question_id = question.id
        elem.question_title = question.title
        elem.date_publish = question.date_publish
        elem.question_tag = tag = question.tag.all()[:2]
        elem.focus_num = question.focus_num
        article = question.article.annotate(Max('thumbsup'))[0]
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', article.content)
        elem.simple_desc=dd
        index_content.append(elem)

    test = range(3)
    return locals()


def index(request):
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
                print u.username, u.sex, u.self_description, u.password, 'user_set'
                client = u
            print client.username, client.sex, client.self_description, client.password, 'client_set'
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
            print name, nickname, phone, pwd, pwd2, sex
            name_dic = verify_username(name)
            phone_dic = verify_phone(phone)
            pwd_dic = verify_pwd(pwd, pwd2)
            dictMerged = dict(name_dic.items() + phone_dic.items() + pwd_dic.items())
            if dictMerged['phone'] == '' and dictMerged['name'] == '' and dictMerged['pwd'] == '':
                user = User()
                user.username = name
                user.nickname = nickname
                user.mobile = phone
                user.password = pwd
                user.sex = sex
                user.save()
            print json.dumps(dictMerged)
            return HttpResponse(json.dumps(dictMerged))
    else:
        return render(request, 'login_reg.html', locals())


@csrf_exempt
def logout(request):
    client = request.session.get('client', default=None)
    print client, 'logout'
    print client.mobile, 'logout'
    if client:
        del request.session['client']
        return HttpResponse('ok')
    else:
        return HttpResponse('please login')


def article(request):
    return render(request, 'article_detail.html', locals())


def profile(request):
    return render(request, 'profile.html', locals())


def inbox(request):
    client = request.session.get('client', default=None)
    message_list = Message.objects.filter(user_id=client.id)
    return render(request, 'inbox.html', locals())
