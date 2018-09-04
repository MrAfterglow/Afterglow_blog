import sys
from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
from datetime import datetime,timedelta
# Create your views here.
from django.urls import reverse
from markdown import markdown
from backweb.models import AType, Article, User, Permission, Role


def login(request):
    if request.method=="GET":
        return render(request,'backweb/login.html')

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #重点！ 验证用户名和密码是否正确
        user = auth.authenticate(request,         #验证成功之后返回当前用户的实例
                                 username=username,
                                 password=password)
        if user:    # 若有user ，表示登陆成功，返回首页
            auth.login(request,user)
            return HttpResponseRedirect(reverse('backweb:index'))
        else:
            return HttpResponseRedirect(reverse('backweb:login'))


def index(request):
    if request.method=="GET":
        #第一种方式，向网页中推数据
        # page_num=request.GET.get()
        # articles=Article.objects.all()[:]

        #第二种 ：
        page_num=int(request.GET.get('page',1))
        articles = Article.objects.all()
        paginator=Paginator(articles,10)
        page=paginator.page(page_num)

        return render(request,'backweb/index.html',{'page':page})


def logout(request):
    if request.method=="GET":
        auth.logout(request)
        return HttpResponseRedirect(reverse('backweb:login'))


def addArt(request):
    if request.method=="GET":
        type=AType.objects.all()
        return render(request,'backweb/article_detail.html',{'types':type})

    if request.method=="POST":
        content=request.POST.get('content')
        title=request.POST.get('title')
        a_type=request.POST.get('a_type')
        desc=request.POST.get('desc')

        img=request.FILES.get('img')

        Article.objects.create(title=title,desc=desc,atype_id=a_type,content=content,image_url=img)
        return HttpResponseRedirect(reverse('backweb:index'))

def delArt(request):
    if request.method=="GET":
        id=request.GET.get('id')
        article=Article.objects.get(id=id)
        article.delete()
        return  HttpResponseRedirect(reverse('backweb:index'))

def my_register(requset):
    if requset.method=="GET":
        return render(requset,'backweb/register.html')

    if requset.method=="POST":
        username=requset.POST.get('username')
        password1=requset.POST.get('password1')
        password2=requset.POST.get('password2')
        db_user=User.objects.filter(username=username).exists()

        if db_user:
            error='账号已存在，请直接登录'
            return render(requset,'backweb/register.html',{'error':error})
        else:
            if password2==password1:
                User.objects.create(username=username,password=password1)
                return HttpResponseRedirect(reverse('backweb:my_login'))
            else:
                error = '两次密码不一致，重新输入'
                return render(requset, 'backweb/register.html', {'error': error})


def my_login(request):
    if request.method=="GET":
        return render(request,'backweb/login.html')

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username,password=password).first()
        if user:
            res=HttpResponseRedirect(reverse('backweb:index'))

            aa='qwertyuiopasdfghjklzxcvbnm123456789'
            session_id=''
            for i in range(20):
                session_id+=random.choice(aa)

            out_time=datetime.now()+timedelta(days=1)
            res.set_cookie('session_id',session_id, expires=out_time)
            user.session_id=session_id
            user.out_time=out_time
            user.save()

            return res
        else:
            error='账号或密码输出错误'
            return render(request,'backweb/login.html',{'error':error})


def my_logout(request):
    if  request.method=="GET":
        user=request.user
        user.session_id=''
        user.save()

        res=HttpResponseRedirect(reverse('backweb:my_login'))
        res.delete_cookie('session_id')
        return res


def add_user(request):
    if request.method=="GET":
        return render(request,'backweb/add_user.html')

    if request.method=="POST":
        username=request.POST.get('username')
        password1=request.POST.get ('password1')
        password2=request.POST.get('password2')

        user=User.objects.filter(username=username).first()
        if user :
            error='账号已经存在啦！'
            return render(request,'backweb/add_user.html',{'error':error})
        else:
            if password1 == password2:
                User.objects.create(username=username, password=password1)
                error = '添加成功'
                return HttpResponseRedirect(reverse('backweb:user_role'))
            else:
                error = '两次密码不一致'
                return render(request,'backweb/add_user.html',{'error':error})


def list_user(request):
    if request.method=="GET":
        users=User.objects.all()
        return  render(request,'backweb/list_user.html',{'users':users})


def role_premission(request):
    if request.method=="GET":
        permission=Permission.objects.all()
        role_all=Role.objects.all()
        return render(request,'backweb/role_premission.html',{'permission':permission,'role_all':role_all})

    if request.method=="POST":
        role_name=request.POST.get('role_name')
        pers=request.POST.getlist('pers')
        try:
            role=Role.objects.get(r_name=role_name)
        except:
            role=Role.objects.create(r_name=role_name)
        for per in pers:
            p=Permission.objects.filter(p_name=per).first()
            role.r_p.add(p)

        return HttpResponseRedirect(reverse('backweb:user_role'))

def user_role(requset):
    if requset.method=="GET":
        user=User.objects.all()
        roles=Role.objects.all()
        return render(requset,'backweb/user_role.html',{
            'roles':roles,
            'users':user
        })


    if requset.method=="POST":
        user_id=requset.POST.get('user')
        role_id=requset.POST.get('role')
        user=User.objects.get(id=user_id)

        user.u_r_id=role_id
        user.save()
        return  HttpResponseRedirect(reverse('backweb:list_user'))


#markdown
