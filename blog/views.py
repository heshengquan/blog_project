from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Category,Post,Tag
import markdown


# Create your views here.
# 首页展示
def index(request):
    post_list=Post.objects.all()



    content={"post_list":post_list}


    return render(request,"blog/index.html",content)

# 博客详情页
def detail(request,id):
    post=get_object_or_404(Post,id=id)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    content={"post":post}
    return render(request,"blog/detail.html",content)

# 归档栏
def archives(request):
    post_list=Post.objects.filter(created_time__year='year',created_time__month='month').order_by("-created_time")

    content = {"post_list": post_list}

    return render(request, "blog/index.html", content)