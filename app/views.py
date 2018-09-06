from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from backweb.models import Article
from rest_framework import mixins,viewsets
from app.app_serializers import ArticleSerializer

class ArticleSource(mixins.ListModelMixin, #查询所有学生
                    mixins.RetrieveModelMixin, #查询指定学生
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin, #更新某个学生
                    mixins.DestroyModelMixin,#删除学生
                    mixins.CreateModelMixin,): #添加学生
    #查询模型的所有数据
    queryset = Article.objects.filter(is_recommend=True)
    #序列化
    serializer_class = ArticleSerializer

    def perform_destroy(self, instance):
        instance.is_read=False
        instance.save()

def index(request):
    if request.method=="GET":
        all_article=Article.objects.filter(is_read=True).order_by('-id')


        return render(request,'web/index.html',{'all_article':all_article})

def about_me(request):
    if request.method=="GET":
        return render(request,'web/about.html')

def slow_life(request):
    if request.method=="GET":
        return render(request,'web/slow_life.html')

def mumble(request):
    if request.method=="GET":
        return render(request,'web/mumble.html')

def dont_stop_learn(request):
    if request.method=="GET":
        return render(request,'web/learn.html')

def content(request):
    if request.method=="GET":
        id=request.GET.get('id')
        article=Article.objects.get(id=id)
        return render(request,'web/content.html',{'article':article})

