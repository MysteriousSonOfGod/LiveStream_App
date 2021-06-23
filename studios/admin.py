from django.contrib import admin
from . import models


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):

    """Studio Admin Definition"""

    list_display = ["name", "get_thumbnail", "count_posts"]

    def __str__(self):
        return self.name

    def count_posts(self, obj):
        return obj.posts.count()

    count_posts.short_description = "Number of Posts"

    def get_thumbnail(self, obj):
        print(dir(obj.image))
        return ""


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    pass
