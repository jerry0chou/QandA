# -*- coding: utf-8 -*-
from django.db.models import Max, Count
from django.test import TestCase
from home.models import Question, User, Tag
from django.db.models import Q
from handle import askQuestion
# Create your tests here.

import datetime
import re


class TestCase(TestCase):
    pass