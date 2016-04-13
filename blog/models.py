from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.



class Article(models.Model):
    title = models.CharField(max_length=15)
    author = models.CharField(max_length=100, default='admin')
    content = models.TextField(max_length=1000)
    hide_content = models.TextField(max_length=1000, default='', blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    description = models.CharField(max_length=200, default='', blank=True)
    # comment = models.ForeignKey(Comment, related_name='article_comment')
    cover = models.CharField(max_length=100, default='/')
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='article_comment')
    content = models.TextField(max_length=1000, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.content


class ZoneSubject(models.Model):
    title = models.CharField(max_length=20, default='')
    image_url = models.CharField(max_length=500)
    create_time = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.image_url


class Search_record(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    searchCount = models.IntegerField(blank=True)
    zhihu_type = models.IntegerField(blank=True)
    def __unicode__(self):
        return self.title

class DoubanTopic(models.Model):
    group_id = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    create_time = models.CharField(max_length=20)
    author_name = models.CharField(max_length=50)
    author_url = models.CharField(max_length=200)
    user_img_small = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title

class ZhihuSubject(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=100)
    zhihu_type = models.IntegerField()
    def __unicode__(self):
        return self.title

class ZhihuQuestion(models.Model):
    subject = models.ForeignKey(ZhihuSubject, related_name='subject_question')
    answer_url = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    author_url = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=100, default='')
    def __unicode__(self):
        return self.title

class ZhihuImage(models.Model):
    question = models.ForeignKey(ZhihuQuestion, related_name='question_image')
    origin_url = models.CharField(max_length=200)
    def __unicode__(self):
        return self.origin_url


class DoubanImage(models.Model):
    topic = models.ForeignKey(DoubanTopic, related_name='topic_image')
    origin_url = models.CharField(max_length=200)
    cos_url =  models.CharField(max_length=200, default='',blank=True)
    type = models.IntegerField(default=0)
    def __unicode__(self):
        return self.origin_url




