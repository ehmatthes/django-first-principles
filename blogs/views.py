from django.shortcuts import render

from .models import Blog, BlogPost


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