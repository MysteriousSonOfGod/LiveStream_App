from django.urls import path
from . import views


app_name = "studios"

urlpatterns = [
    path("", views.my_studio, name="studio"),
    path("posts", views.PostView.as_view(), name="posts"),
    path("posts/<str:id>", views.detail, name="post_detail"),
    path("posts/new/", views.new, name="post_new"),
    path("posts/create/", views.create, name="post_create"),
    path("posts/edit/<str:id>", views.edit, name="post_edit"),
    path("posts/update/<str:id>", views.update, name="post_update"),
    path("posts/delete/<str:id>", views.delete, name="post_delete"),
    path("my_page", views.my_page, name="my_page"),
]
