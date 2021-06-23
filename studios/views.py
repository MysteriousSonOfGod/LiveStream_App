from django.db import close_old_connections
import channels
from studios import models
from django.shortcuts import render
from django.views.generic import ListView


def MyStudio(request):
    return render(request, "studios/my_studio.html")


def my_page(request):
    return render(request, "studios/my_page.html")


class PostView(ListView):

    """PostView Definition"""

    model = models.Post
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"
