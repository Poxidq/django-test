from django.utils.timezone import now
from django.shortcuts import render, redirect
from .models import Post


def index(request):
    post_objects = Post.objects.all()
    context = {
        "posts": post_objects,
    }
    return render(request, "posts/index.html", context)


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/detail.html", {"post": post})


def update(request, post_id):
    if request.method == "POST":
        post_object = Post.objects.get(id=post_id)
        post_object.title = request.POST["title"]
        post_object.body = request.POST["body"]
        post_object.pub_date = now()
        post_object.save()
    return redirect(detail, post_id)
