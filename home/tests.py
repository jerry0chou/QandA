# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import *
from django.db.models import Q

# Create your tests here.

import datetime
import re

class TestCase(TestCase):
    user=User.objects.get(id=2)
    user.sex='女'
    user.email='1052757325@qq.com'
    user.password='456789'
    user.save()