#coding:utf-8
from django.shortcuts import render, HttpResponse, Http404
from blog.models import Article, ZoneSubject
# Create your views here.


def home(request, page=None):
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
    return render(request, 'index.html', {'index': 1, 'data': data, 'current_page': page, 'item_count': item_count})


def article_page(request, parm):
    try:
        find_article = Article.objects.get(id=parm)
    except ValueError, e:
        find_article = None
    if find_article:
        article = {
            'title': find_article.title,
            'create_time': find_article.create_time,
            'content': find_article.content,
            'hide_content': find_article.hide_content
        }
        return render(request, "article.html", {'index': 1, 'article': article, 'title': find_article.title})
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
    return render(request, 'zone.html', {'index': 3, 'item_count': count, 'current_page': page, 'data': data})