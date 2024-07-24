from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def home_page(request):
    return render(request, "home_page.html")

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        "post":post
    }
    return render(request, "post_detail.html", context)

def create_post(request):
    if request.method == "GET":
        form = PostForm()
        context = {
            "form":form,
            "post":None
        }
        return render(request, "post_form.html", context)
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post_instance = form.save()
            return redirect("post_detail", post_id=post_instance.id)

def edit_post(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    if request.method == "GET":
        form = PostForm(instance=post)
        context = {
            "form":form,
            "post":post
        }
        return render(request, "post_form.html",context)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post_instance = form.save()
            return redirect("post_detail",post_id=post_instance.id)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method=="GET":
        context = {
            "post":post
        }
        return render(request, "delete_post.html", context)
    else:
        post.delete()
        return redirect("post_list")


