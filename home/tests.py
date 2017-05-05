# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *

# Create your tests here.

import datetime


class inbox:
    def __init__(self):
        self.from_user = None
        self.to_user = None
        self.message_text = ''


class TestCase(TestCase):
    follow_users=[]
    follow_list = Follow.objects.filter(follower_id=2)
    for follow in follow_list:
        user=User.objects.get(id=follow.followee_id)
        follow_users.append(user)



