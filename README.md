# Afterglow_blog
This's my blog,use Python_Django ,MySql, restful even more



### 7.20日：

......

......

......

### 9.6日：

很久没动博客了，上一次数据库崩了就没整它，今天抽空把数据库重新整了一下，中途问题出现很多，在本地pc迁移数据到云服务器的时候，有一个外键关联始终有问题，于是折腾了许久，最后终于搞定了。

修改了文章模型，去除了一个重复的字段，修改了一些后台的网页代码。


### 9.7日：

完成了后台的的index修改： 点击文章的是否推荐和是否展示按钮后，改变文章对象的is_recommend和is_read的值，并在页面上ajax异步刷新。

修改了前端页面的主要风格： 修改了背景图片，修改了整体色调。

修改了推荐文章的背景图片和路由地址。

### 9.8日：

优化了learn.html中时间的格式化，

```
<time class="cbp_tmtime"><span> {{art.oprate_time | date:'h-d'}} </span> <span>{{art.oprate_time | date:'Y'}}</span></time>
```

优化了learn.html中的page分页

### 9.10:

完成了“学无止境“ 板块 ，

### 9.11:

完成了“慢生活” 板块 

项目大体完成。