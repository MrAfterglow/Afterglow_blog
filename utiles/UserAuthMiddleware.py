from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from backweb.models import User
import re

class AuthMiddleWare(MiddlewareMixin):

    def process_request(self,request):

        path=request.path   #这个就是request里面的网页地址
        if re.match(r'/backweb/(\S+)', path):
            if path=='/backweb/my_login/' :
                return None #当 当前地址就是login的时候，说明已近验证过下面两条，都不符合，需要登录了。
            session_id=request.COOKIES.get('session_id') #本地没有cookie
            if not session_id :
                return HttpResponseRedirect(reverse('backweb:my_login'))

            user=User.objects.filter(session_id=session_id).first()#本地有，但服务器没有与之对应的session
            if not user:
                 return HttpResponseRedirect(reverse('backweb:my_login'))

            user.permission_all=[p.p_name for p in user.u_r.r_p.all() ]
            request.user=user
            return None #上面两条都不成立，说明网页cookie和库中session相同，可以跳过登录直接进入系统