from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import *
from .forms import *
def post_details(request):
    context={}
    post_obj=Post.objects.all()
    context["post_obj"]=post_obj 
    return render(request,'blog_post/post_details.html', {'post_obj': post_obj})
  
def post_add(request):
    context={}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_created_obj = form.save()
            return redirect('post_details')
        else:
            messages.info(request,form.error())            
    else:
        context["form"]=PostForm()  
        return render(request,"blog_post/post_add.html",context)

def post_edit(request,id=None):
    context={}
    post_obj = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post_obj)
        if form.is_valid():
            post_updated_obj = form.save()
            return redirect('post_details')
    else:
        context["form"]=PostForm(instance=post_obj)   
        return render(request,"blog_post/post_add.html",context)

def post_delete(request,id=None):
    context = {}
    post_obj = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        post_obj.delete()
        return redirect('post_details')
    else:
        context['post_obj'] = post_obj
        return render(request, 'blog_post/post_delete.html', context)

def post_wise_details(request,id=None):
    context={}
    post_obj = get_object_or_404(Post, pk=id)
    context["post_obj"]=post_obj 
    return render(request,'blog_post/post_wise_details.html', {'post_obj': post_obj})  

def comment_add(request,id=None):
    context={}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_created_obj = form.save(commit=False)
            post_obj = get_object_or_404(Post, pk=id)
            comment_created_obj.post=post_obj
            comment_created_obj.save()
            return redirect('post_wise_details',id=id)
        else:
            messages.info(request,form.error())            
    else:
        context["form"]=CommentForm()  
        return render(request,"blog_post/comment_add.html",context)

def comment_edit(request,id=None):
    context={}
    comment_obj = get_object_or_404(Comment, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=comment_obj)
        if form.is_valid():
            post_updated_obj = form.save()
            return redirect('post_wise_details',id=comment_obj.post.id)
    else:
        context["form"]=CommentForm(instance=comment_obj)   
        return render(request,"blog_post/post_add.html",context)