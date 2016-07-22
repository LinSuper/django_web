from django.contrib import admin
from blog.models import (
    Article,
    Comment,
    ZoneSubject,
    Search_record,
    DoubanTopic,
    DoubanImage,
    ZhihuSubject,
    ZhihuQuestion,
    ZhihuImage
)

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'description','cover', 'create_time', 'author','visible') # list
    inlines = [CommentInline,]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'article')

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'title', 'image_url')

class SeachRecordAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'searchCount', 'zhihu_type']

class DoubanImageInline(admin.TabularInline):
    model = DoubanImage

class DoubanTopicAdmin(admin.ModelAdmin):
    inlines = [DoubanImageInline,]
    list_display = ['title', 'group_id', 'url', 'author_url', 'create_time']

class DoubanImageAdmin(admin.ModelAdmin):
    list_display = ['topic', 'origin_url', 'type']

class ZhihuImageInline(admin.TabularInline):
    model = ZhihuImage

class ZhihuQuestionInline(admin.TabularInline):
    model = [ZhihuQuestion,]

class ZhihuImageAdmin(admin.ModelAdmin):
    list_display = ['question', 'origin_url']

class ZhihuQuestionAdmin(admin.ModelAdmin):
    inlines = [ZhihuImageInline,]
    list_display = ['subject', 'title', 'answer_url', 'author']

class ZhihuSubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'zhihu_type']
    # inlines = [ZhihuQuestionInline,]


admin.site.register(ZhihuSubject, ZhihuSubjectAdmin)
admin.site.register(ZhihuQuestion, ZhihuQuestionAdmin)
admin.site.register(ZhihuImage, ZhihuImageAdmin)
admin.site.register(DoubanImage, DoubanImageAdmin)
admin.site.register(DoubanTopic, DoubanTopicAdmin)
admin.site.register(Search_record, SeachRecordAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ZoneSubject, ZoneAdmin)