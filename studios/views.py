from typing import NewType
from django.db import close_old_connections
import channels
from studios import models
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.utils import timezone
from . import models
import studios


def my_studio(request):
    category = models.Category.objects.all()
    return render(request, "studios/my_studio.html", {"category": category})


def my_page(request):
    return render(request, "studios/my_page.html")


class PostView(ListView):

    """PostView Definition"""

    model = models.Post
    paginate_by = 5
    # paginate_orphans = 2
    ordering = "created"
    context_object_name = "posts"


def detail(request, id):
    post = get_object_or_404(models.Post, id=id)
    return render(request, "studios/post_detail.html", {"post": post})


def new(request):
    return render(request, "studios/post_new.html")


def create(request):
    new_post = models.Post()
    new_post.title = request.POST["title"]
    new_post.writer = request.user
    new_post.body = request.POST["body"]
    new_post.created = timezone.now()
    new_post.save()

    return redirect("studios:post_detail", new_post.id)


def edit(request, id):
    edit_post = models.Post.objects.get(id=id)

    return render(request, "studios/post_edit.html", {"post": edit_post})


def update(request, id):
    update_post = models.Post.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.writer = request.user
    update_post.body = request.POST["body"]
    update_post.updated = timezone.now()
    update_post.save()

    return redirect("studios:post_detail", update_post.id)


def delete(request, id):
    delete_post = models.Post.objects.get(id=id)
    delete_post.delete()
    return redirect("studios:posts")
