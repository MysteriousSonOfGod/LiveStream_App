from django.db import models
from core import models as core_model


class Channel(core_model.TimeStampedModel):

    """Channel Model Definition"""

    name = models.CharField(max_length=140)
    on_air = models.BooleanField(default=False)

    def __str__(self):
        return self.name
