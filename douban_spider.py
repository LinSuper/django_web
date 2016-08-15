# coding: utf-8

from douban import Discussion
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_web.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

from blog.models import DoubanImage, DoubanTopic

discussion_dict = {
    'meituikong': 'https://www.douban.com/group/meituikong',
    #'510760': 'https://www.douban.com/group/510760', #96
    #'516876':'https://www.douban.com/group/516876',
    'haixiuzu':'https://www.douban.com/group/haixiuzu/' #36
}


def init():
    for k, v in discussion_dict.iteritems():
        print v
        discussion = Discussion(v)
        topics = discussion.get_top_i_page_topic(10)
        for topic in topics:
            print topic.topic_url
            image_list = topic.get_image()
            for j in image_list:
                author = topic.get_author()
                find_img = DoubanImage.objects.filter(origin_url=j).all()
                find_topic = DoubanTopic.objects.filter(url=topic.topic_url).all()
                if len(find_img) == 0:
                    tmp_img = DoubanImage(
                        origin_url=j
                    )
                    if(len(find_topic)>0):
                        tmp_img.topic = find_topic[0]
                    else:
                        tmp_topic = DoubanTopic(
                            group_id = k,
                            url = topic.topic_url,
                            title = topic.title,
                            create_time = topic.create_time,
                            author_name = author.user_name,
                            author_url = author.user_url,
                            user_img_small = ''
                        )
                        tmp_topic.save()
                        tmp_img.topic = tmp_topic
                    tmp_img.save()
                    print "insert", tmp_img

init()
