from django.contrib import admin
from .models import BlogArticles    # 将models模块中的 BlogArticles 类导入当前空间


#  自定义数据显示类
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")   # 设置包要显示的字段名的元组
    list_filter = ("publish", "author")  # 给用户自定义分类查询的接口
    search_fields = ('title', 'body')  # 在列表的顶部增加一个搜索框
    raw_id_fields = ("author",)        # 显示外键的详细信息
    date_hierarchy = "publish"         # 详细时间筛选
    ordering = ['-publish', 'author']  # 对象默认的顺序，获取一个对象的列表时使用 '-'为倒序大到小




admin.site.register(BlogArticles, BlogArticlesAdmin)   # 通过代码将BlogArticles注册到admin中
# Register your models here.
