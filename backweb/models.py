from django.db import models

# Create your models here.

from django.db import models
from DjangoUeditor3.DjangoUeditor.models import UEditorField

class AType(models.Model):
    name = models.CharField(max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'AType'


class Article(models.Model):
    title= models.CharField(max_length=15,null=False)
    desc=models.CharField(max_length=50,null=False)
    is_read = models.BooleanField(default=True)
    is_recommend=models.BooleanField(default=False)
    is_learn=models.BooleanField(default=True)
    content=UEditorField(default=True)
    image_url=models.ImageField(upload_to='upload',null=True)
    #统计recommend文件是否超过3个：
    recommend_count=models.IntegerField(null=True)


    atype=models.ForeignKey(AType,null=True)

    create_time=models.DateTimeField(auto_now_add=True)
    oprate_time=models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'

class Permission(models.Model): #权限表  和角色表多对多
    p_name = models.CharField(max_length=15)

    class Meta:
        db_table='permission'


class Role(models.Model):  # 角色表 和权限表多对多，和用户表一对一
    r_name = models.CharField(max_length=10)
    r_p = models.ManyToManyField(Permission)

    class Meta:
        db_table = 'role'


class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    session_id=models.CharField(max_length=30,null=True)
    out_time=models.DateTimeField(null=True)
    is_superuser=models.BooleanField(default=0)
    u_r=models.ForeignKey(Role ,null=True)

    class Meta:
        db_table='user'




#markdown编辑器




