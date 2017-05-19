# -*- coding: utf-8 -*-
from models import *
from django.contrib import admin


# Register your models here.
class UserleAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname', 'sex', 'self_description', 'email', 'mobile')
    list_display_links = ('username',)
    list_filter = ('username', 'email',)
    fieldsets = (
        (None, {
            'fields': ('profile','username', 'nickname', 'sex', 'self_description', 'email', 'mobile', 'password',)
        }),

    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/profile.js',
        )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'thumbsup', 'date_publish',)
    list_display_links = ('user',)
    list_filter = ('date_publish', 'thumbsup')


    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'date_publish', 'thumbsup',)
    list_display_links = ('content',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'content', 'date_publish',)
    list_display_links = ('content',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','desc', 'date_publish', 'likes',)
    list_display_links = ('title',)
    list_filter = ('date_publish', 'likes')

admin.site.register(User, UserleAdmin)
admin.site.register(Follow)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
