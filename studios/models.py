from typing import Text
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from core import models as core_models
from users import models as user_models


class Studio(core_models.TimeStampedModel):

    """Studio Model Definition"""

    name = models.CharField(max_length=200, null=True)
    desc = models.TextField(blank=True)
    image = ImageField(blank=True)
    posts = models.ManyToManyField("Post", related_name="posts", blank=True)


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    title = models.CharField(max_length=200, null=True)
    writer = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, null=True
    )
    body = models.TextField(blank=True)
