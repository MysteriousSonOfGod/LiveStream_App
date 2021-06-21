from django.db import models
from django_countries.fields import CountryField
from core import models as core_model
from users import models as user_model


class Channel(core_model.TimeStampedModel):

    """Channel Model Definition"""

    name = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    country = CountryField(blank_label="(select country)", multiple=True, blank=True)
    on_air = models.BooleanField(default=False)
    artist = models.ForeignKey(user_model.User, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField("Genre", related_name="channels", blank=True)
    resolution = models.ForeignKey("Resolution", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class AbstractItem(core_model.TimeStampedModel):

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
