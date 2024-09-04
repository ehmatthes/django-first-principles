from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


def index(request):
    return render(request, "blogs/index.html")

def blogs(request):
    all_blogs = Blog.objects.all()
    context = {"blogs": all_blogs}
    return render(request, "blogs/blogs.html", context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()
    
    context = {
        "blog": blog,
        "posts": posts,
    }
    return render(request, "blogs/blog.html", context)

def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog

    context = {
        "post": post,
        "blog": blog,
    }
    return render(request, "blogs/post.html", context)

@login_required
def new_blog(request):
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect("blogs:blogs")

    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)

@login_required
def new_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    # Only allow blog owners to add new posts.
    if request.user != blog.owner:
        return redirect("blogs:index")

    if request.method != "POST":
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect("blogs:blog", blog_id)

    context = {"form": form, "blog": blog}
    return render(request, "blogs/new_post.html", context)