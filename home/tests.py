# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *
from django.db.models import Q

# Create your tests here.

import datetime


class TestCase(TestCase):
    u = User.objects.get(id=2)
    message = Message.objects.filter(Q(from_user=u) | Q(to_user=u)).order_by('-date_publish')
    # for m in message:
    #     print unicode(m.from_user.nickname),unicode(m.to_user.nickname),unicode(m.content[:5]),m.date_publish