#coding:utf-8
from django.shortcuts import render, HttpResponse, Http404, HttpResponsePermanentRedirect
from blog.models import (
    Article,
    ZoneSubject,
    DoubanTopic,
    ZhihuSubject,
    Search_record,
    Comment
)
from django.contrib.auth.models import User
# Create your views here.


def home(request, page=None):
    if request.get_host() != 'www.kantujun.com':
        return HttpResponsePermanentRedirect('http://www.kantujun.com')
    if page is None:
        page = 1
        start = 0
        end = 5
    else:
        page = int(page)
        start = (page - 1) * 5
        end = page * 5
    item_count = Article.objects.count()
    get_articles = Article.objects.order_by('-create_time').all()[start:end]
    data = []
    for i in get_articles:
        data.append({
            'title': i.title,
            'cover': i.cover,
            'description': i.description,
            'create_time': i.create_time,
            'author': i.author,
            'id': i.id
        })
    return render(request, 'index.html', {
        'index': 1, 'data': data, 'current_page': page, 'item_count': item_count,
        'title': u'豆瓣妹子福利 － 知乎福利'
    })


def article_page(request, parm):
    try:
        find_article = Article.objects.get(id=parm)
    except ValueError, e:
        find_article = None
    if find_article:
        article = {
            'id': find_article.id,
            'title': find_article.title,
            'create_time': find_article.create_time,
            'content': find_article.content,
            'hide_content': find_article.hide_content
        }
        article_comment = find_article.article_comment.all()
        comments = []
        comments_user_id = [i.user_id for i in article_comment]
        find_user = User.objects.filter(id__in=comments_user_id).all()
        user_dict = {str(i.id): i.username for i in find_user}
        for i in article_comment:
            comments.append({
                'username': user_dict[i.user_id],
                'content': i.content,
                'create_time': i.create_time
            })

        return render(request, "article.html",{
            'index': 1, 'article': article, 'title': find_article.title, 'comments':comments
        })
    else:
        raise Http404(u"非法路径！！！")

def get_me_a_tip(request):
    return render(request, "tip.html", {'index': 4, 'title': u'打赏我'})

def zhihu_page(request, page=None):
    return render(request, 'zhihu.html', {'index': 3})


def zone_page(request, page=None):
    if page:
        page = int(page)
        start = (page - 1) * 5
        end = page * 5
    else:
        page = 1
        start = 0
        end = 5
    count = ZoneSubject.objects.count()
    find_zone = ZoneSubject.objects.order_by('-create_time').all()[start:end]
    data = []
    for i in find_zone:
        data.append({
            'title': i.title,
            'create_time': i.create_time,
            'content': i.image_url
        })
    return render(request, 'zone.html', {'index': 3, 'item_count': count, 'current_page': page, 'data': data, 'title': u'捡图'})


def douban_page(request, page=None):
    if page:
        page = int(page)
        start = (page - 1) * 20
        end = page * 20
    else:
        page = 1
        start = 0
        end = 20
    count = DoubanTopic.objects.filter(visible=True).count()
    find_douban = DoubanTopic.objects.filter(visible=True).order_by('-create_time').all()[start:end]
    data = []
    for n, i in enumerate(find_douban):
        if n % 4 == 0:
            data.append([])
        if i.topic_image.count()==0:
            i.delete()
            continue
        image_url = i.topic_image.first()
        data[-1].append({
            'author_url': i.author_url,
            'author_name': i.author_name,
            'url': i.url,
            'image_url': image_url.origin_url
        })
    return render(request, 'douban.html', {
        'index': 5, 'item_count': count, 'current_page': page, 'data': data, 'title': u'豆瓣妹子'
    })

def zhihu_page(request, page=None):
    if 'question' in request.get_full_path():
        type = 1
    else:
        type = 0
    if page:
        page = int(page)
        start = (page - 1) * 5
        end = page * 5
    else:
        page = 1
        start = 0
        end = 5
    count = Search_record.objects.filter(zhihu_type=type).count()
    find_search_records = Search_record.objects.order_by('-searchCount').filter(zhihu_type=type).all()[start:end]
    url_list = [i.url for i in find_search_records]
    find_items = ZhihuSubject.objects.filter(url__in=url_list)
    data = []
    for i in find_items:
        image_list = []
        question = i.subject_question.iterator()
        for j in question:
            image_list += [z.origin_url for z in j.question_image.all()]
            if len(image_list) >= 5:
                image_list = image_list[:5]
                break
        data.append({
            'id': i.id,
            'url': i.url,
            'title': i.title,
            'image': image_list

        })
    return render(request, 'zhihu_page.html', {'data': data, 'current_page': page, 'item_count':count, 'type': type, 'title': u'知乎看图'})


def zhihu_detail_page(request, d_id, page=None):
    if page:
        page = int(page)
        start = (page - 1) * 5
        end = page * 5
    else:
        page = 1
        start = 0
        end = 5
    find_subject = ZhihuSubject.objects.filter(id=d_id)[0]
    find_search_item = Search_record.objects.filter(url=find_subject.url)[0]
    find_search_item.searchCount += 1
    find_search_item.save()
    type = find_subject.zhihu_type
    title = find_subject.title
    url = find_subject.url
    count = find_subject.subject_question.count()
    find_item = find_subject.subject_question.all()[start:end]
    data = []
    for i in find_item:
        image = i.question_image.all()
        image_url = [j.origin_url for j in image]
        data.append({
            'answer_title': i.title,
            'author_url': i.author_url,
            'author': i.author,
            'answer_url': i.answer_url,
            'image': image_url
        })
    return render(request, 'zhihu_detail.html', {
        'title': title, 'url': url, 'data': data, 'type': type, 'item_count': count,
        'current_page':page, 'id': d_id
    })
