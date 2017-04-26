# -*- coding: utf-8 -*-
from models import *
from django.contrib import admin


# Register your models here.
class UserleAdmin(admin.ModelAdmin):
    list_display = ('username','nickname', 'sex', 'self_description', 'email', 'mobile')
    list_display_links = ('username',)
    list_filter = ('username', 'email',)
    fieldsets = (
        (None, {
            'fields': ('username','nickname', 'sex', 'self_description', 'email', 'mobile', 'password',)
        }),

    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'desc', 'thumbsup',)
    list_display_links = ('title',)
    list_filter = ('date_publish', 'title')
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'thumbsup', 'content', 'tag', 'user', 'date_publish',)
        }),
    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date_publish', 'thumbsup',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'date_publish',)
    list_display_links = ('content',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

admin.site.register(User, UserleAdmin)
admin.site.register(Follow)
admin.site.register(Tag,TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Message,MessageAdmin)
