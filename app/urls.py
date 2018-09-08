from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from app import views

router=SimpleRouter()
router.register('article', views.ArticleSource) #(资源，方法）


urlpatterns = [
    url(r'index/',views.index ,name='index'),
    url(r'about_me/',views.about_me,name='about_me'),
    url(r'mumble/',views.mumble,name='mumble'),
    url(r'dont_stop_learn/',views.dont_stop_learn,name='dont_stop_learn'),
    url(r'content/',views.content,name='content'),
    url(r'life/',views.life,name='life'),

]
urlpatterns+=router.urls
