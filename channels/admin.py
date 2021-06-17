from django.contrib import admin
from . import models


@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):

    """Channel Admin Definition"""

    list_display = [
        "name",
        "on_air",
    ]

    list_filter = ("on_air",)
