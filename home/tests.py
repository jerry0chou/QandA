# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *

# Create your tests here.

import datetime

class TestCase(TestCase):
    # u=User.objects.get(id=2)
    # message=Message.objects.
    # for m in message:
    #     print unicode(m.from_user.nickname),unicode(m.content)
