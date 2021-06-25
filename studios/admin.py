from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    """Category Admin Definition"""

    list_display = ("name",)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    list_display = [
        "title",
        "writer",
        "p_studio",
    ]

    list_filter = (
        "writer",
        "p_studio",
    )


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):

    """Studio Admin Definition"""

    list_display = [
        "name",
        "studio_host",
        "count_posts",
        "get_thumbnail",
    ]

    raw_id_fields = ("studio_host",)

    def count_posts(self, obj):
        return obj.posts.count()

    count_posts.short_description = "Number of Posts"

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.image.url}" />')

    get_thumbnail.short_description = "Thumbnail"
