from django.contrib import admin
from . import models


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):

    """Studio Admin Definition"""

    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    pass
