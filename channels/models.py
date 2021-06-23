from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class Channel(core_models.TimeStampedModel):

    """Channel Model Definition"""

    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to="channel_photos", blank=True)
    country = CountryField()
    on_air = models.BooleanField(default=False)
    genre = models.ManyToManyField("Genre", blank=True)
    resolution = models.ForeignKey("Resolution", on_delete=models.SET_NULL, null=True)
    channel_host = models.ForeignKey(
        "users.User",
        related_name="channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item Model Definition"""

    name = models.CharField(max_length=80)

    class meta:
        abstract = True

    def __str__(self):
        return self.name


class Genre(AbstractItem):

    """Genre Model Definition"""

    pass


class Resolution(AbstractItem):

    """Resolution Model Definition"""

    pass
