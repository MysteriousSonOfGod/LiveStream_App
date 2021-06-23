from django.urls import path
from . import views


app_name = "studios"

urlpatterns = [
    path("", views.MyStudio, name="studio"),
    path("posts", views.PostView.as_view(), name="posts"),
    path("posts/<str:post_id>", views.detail, name="post_detail"),
    path("posts/new/", views.new, name="post_new"),
    path("posts/create/", views.create, name="post_create"),
    path("my_page", views.my_page, name="my_page"),
]
