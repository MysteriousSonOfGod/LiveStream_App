from django.urls import path
from . import views

app_name = "studios"

urlpatterns = [
    path("", views.MyStudio, name="studio"),
    path("posts", views.Posts, name="posts"),
    path("my_page", views.my_page, name="my_page"),
]
