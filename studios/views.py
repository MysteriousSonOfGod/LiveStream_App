from studios import models
from django.shortcuts import render


def MyStudio(request):
    return render(request, "studios/mystudio.html")
