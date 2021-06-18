from django.urls import path
from channels import views as channel_views

app_name = "core"

urlpatterns = [path("", channel_views.home, name="home")]
