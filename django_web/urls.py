"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views  as blog_vies
from api import views as api_view




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/(.+)/$', blog_vies.article_page),
    url(r'^home/(.+)/$|^$', blog_vies.home),
    url(r'^give_me_tip/$', blog_vies.get_me_a_tip),
    url(r'^zhihu/question/$|^zhihu/question/(.+)/$', blog_vies.zhihu_page),
    url(r'^zhihu/collection/$|^zhihu/collection/(.+)/$', blog_vies.zhihu_page),
    url(r'^api/test/$', api_view.api_test),
    url(r'^zone/$|^zone/(.+)/$', blog_vies.zone_page),
    url(r'^img/sign$', api_view.sign),
    url(r'^api/upload_api$', api_view.upload_api),
    url(r'^img/zhihu$', api_view.return_zhihu_img),
    url(r'^img/douban$', api_view.return_douban_img),
    url(r'^douban$|^douban/(.+)/$', blog_vies.douban_page),
    url(r'^zhihu/detail/(.+)/(\d+)/$', blog_vies.zhihu_detail_page),
    url(r'^zhihu/detail/(.+)/$', blog_vies.zhihu_detail_page),
    url(r'^api/zhihu_spider$', api_view.insert_search)
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
