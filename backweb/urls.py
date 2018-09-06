from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from backweb import views

# login_required()   #登录需要

urlpatterns = [
    #django 自带的：
    # url(r'login',views.login,name='login'),
    url(r'index/',views.index,name='index'),
    # url(r'logout/',views.logout,name='logout'),
    # url(r'add/',views.add,name='add'),
    url(r'addArt/',views.addArt,name='addArt'),

    #自己实现登录注册注销
    url(r'^my_login/',views.my_login,name='my_login'),  #登录
    url(r'my_register/',views.my_register,name='my_register') ,#注册
    url(r'my_logout/', views.my_logout, name='my_logout'),  # 注销
    url(r'delArt/',views.delArt ,name='delArt'),

    #装饰器
    url(r'add_user/',views.add_user,name='add_user'),
    url(r'list_user/',views.list_user,name='list_user'),
    url(r'role_premission/',views.role_premission,name='role_premission'),  #角色和权限关系
    url(r'user_role/',views.user_role,name='user_role'), #用户角色管理
    url(r'change_is_read/',views.change_is_read,name='change_is_read'),


]