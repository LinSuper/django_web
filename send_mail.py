#coding:utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_web.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django, re
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from django.contrib.auth.models import User
from django.core.mail import send_mail


u = User.objects.all()
regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)


user_list = []
for i in u:
    email = i.email
    mails = re.findall(regex, email)
    user_list += mails

send_mail(u'看图君', u'主页更新了，清纯的韩国小女神<a href="http://www.kantujun.com/article/21/">链接</a>', '8674925@163.com', user_list)
