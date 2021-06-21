from django.urls import path
from . import views

app_name = "studios"

urlpatterns = [path("studio", views.MyStudio, name="studios")]
