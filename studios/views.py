from studios import models
from django.shortcuts import render


def MyStudio(request):
    return render(request, "studios/mystudio.html")


def Posts(request):
    posts = models.Post.objects.all()
    return render(request, "studios/posts_list.html", {"posts": posts})


def my_page(request):
    return render(request, "studios/my_page.html")
