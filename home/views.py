# -*- coding: utf-8 -*-
import json

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from handle import getSequence, showPage, getMostReply, getArticleCommet, saveComment, sendMessage, getFollowId, getProfile
from home.models import User, Follow, Message, Question
from home.verify import verify_username, verify_phone, verify_pwd


def global_setting(request):
    client = request.session.get('client', default=None)

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
    num = request.GET.get('num')

    Qlist = Question.objects.all().order_by('-likes')  # 查询
    length = len(Qlist)
    result = getSequence(length, 2)  # 每两个为一页
    size = range(len(result))  # 这个是列表
    length = len(size)

    if num is None:
        pagenum = 1
        index_content = showPage(Qlist, result, 0)
    else:
        try:
            pagenum = int(num)
            if pagenum - 1 in size:
                index_content = showPage(Qlist, result, pagenum - 1)
        except Exception:
            print Exception.message, '类型转换有问题'

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
            dictMerged = dict(name_dic.items() + phone_dic.items() + pwd_dic.items())
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
            foll = Follow.objects.get(follower_id=int(followerId), followee_id=followeeIid)
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
        sendMessage(from_id=from_user_id, to_id=to_user_id, content=message_text)
        return HttpResponse('ok')

@csrf_exempt
def profile(request):
    uid = request.GET.get('uid')
    if uid:
        # followUsers = getFollowUsers(fid=uid)
        profile=getProfile(uid)
        return render(request, 'profile.html', locals())


@csrf_exempt
def inbox(request):
    client = request.session.get('client', default=None)
    if client:
        message_list = Message.objects.filter(from_user_id=client.id)
    return render(request, 'inbox.html', locals())
