from django.conf.urls  import url
from . import views


urlpatterns =[
    url(r"^$", views.blog_title, name="blog_title"),    # 将views中的blog_title类调用
    url(r'(?P<article_id>\d)/$', views.blog_article, name="blog_detail")
]