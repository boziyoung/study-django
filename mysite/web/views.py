from django.shortcuts import render, get_object_or_404   # 将django.shortcuts模块中的方面render, get_object_or_404 导入指定空间
from .models import BlogArticles

# 获取博客的标题 书25-26 page
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "web/titles.html", {"blogs":blogs})

# 获取博客内容
def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "web/content.html", {"article":article, "publish": pub } )


# Create your views here.
