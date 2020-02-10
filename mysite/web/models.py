"""
数据模型设置
"""
from django.db import models   # 把django模块中的models语句导入指定空间
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)    # 规定了title 的属性为chairfiled类型，并且设置了字段最大数量
    author = models.ForeignKey(User, related_name="web_posts")  # author规定了博客文章和用户之间的关系，一个用户对应多个文章
    body = models.TextField()
    publish = models.DateField(default=timezone.now)


    class Meta:
        ordering = ("-publish",)    # 规定了BlogArticles 实列对象显示顺序，即按照publish字段倒序显示

    def __str__(self):
        return self.title
