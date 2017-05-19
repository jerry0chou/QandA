"""QandA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from QandA import settings
from home import views
from home.upload import upload_image

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r"^uploads/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT, }),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),

    url(r'^$', views.index, name='index'),
    url(r'^login_reg/$', views.login_reg, name='login_reg'),
    url(r'^article/$', views.article, name='article'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^logout/$', views.logout, name='logout'),

    url(r'^ask/$', views.ask, name='ask'),
    url(r'^answer/$', views.answer, name='answer'),

]
