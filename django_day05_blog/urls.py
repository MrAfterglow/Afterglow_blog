"""django_day05_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static   #将media变成类型static的静态目录，

from app import views
from django_day05_blog import settings
urlpatterns = [

    url(r'blog/',include('app.urls',namespace='blog')),
    url(r'^$',views.index),
    url(r'backweb/',include('backweb.urls',namespace='backweb')),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #将media变成类型static的静态目录，
