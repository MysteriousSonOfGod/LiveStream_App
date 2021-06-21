from django.contrib import admin
from . import models


@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):

    """Channel Admin Definition"""

    list_display = [
        "name",
        "artist",
        "country",
        "resolution",
        "on_air",
    ]

    list_filter = ("on_air", "genre", "resolution")


@admin.register(models.Genre, models.Resolution)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass
