from typing import Text
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from core import models as core_models
from users import models as user_models


class StudioAbstractItem(core_models.TimeStampedModel):

    """Abstract Item Model Definition"""

    name = models.CharField(max_length=80)

    class meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(StudioAbstractItem):

    """Category Model Definition"""

    pass


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    title = models.CharField(max_length=200, null=True)
    writer = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE, null=True
    )
    body = models.TextField(blank=True)
    p_studio = models.ForeignKey(
        "Studio", related_name="posts", on_delete=models.CASCADE, blank=True, null=True
    )
    category = models.ForeignKey(
        "Post", related_name="posts", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title


class Studio(core_models.TimeStampedModel):

    """Studio Model Definition"""

    name = models.CharField(max_length=200, null=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="studio_photos", blank=True, null=True)
    studio_host = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
