from typing import NewType
from django.db import close_old_connections
import channels
from studios import models
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.utils import timezone
from . import models


def MyStudio(request):
    return render(request, "studios/my_studio.html")


def my_page(request):
    return render(request, "studios/my_page.html")


class PostView(ListView):

    """PostView Definition"""

    model = models.Post
    paginate_by = 5
    # paginate_orphans = 2
    ordering = "created"
    context_object_name = "posts"


def detail(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
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
