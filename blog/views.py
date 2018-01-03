from django.shortcuts import render,redirect,get_object_or_404
from blog.models import Category,Post,Tag


# Create your views here.

def index(request):
    post_list=Post.objects.all()

    content={"post_list":post_list}


    return render(request,"blog/index.html",content)


def detail(request,id):
    post=get_object_or_404(Post,id=id)
    content={"post":post}
    return render(request,"blog/detail.html",content)