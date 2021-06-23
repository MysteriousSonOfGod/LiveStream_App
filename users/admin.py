from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from . import models
from channels import models as channel_models
from studios import models as studio_models


class ChannelInline(admin.TabularInline):

    model = channel_models.Channel


class StudioInline(admin.TabularInline):

    model = studio_models.Studio


@admin.register(models.User)
class CustomAdminUser(UserAdmin):

    """Custom User Admin Definition"""

    inlines = (
        ChannelInline,
        StudioInline,
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "nickname",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "busker",
                )
            },
        ),
    )

    list_display = [
        "username",
        "nickname",
        "gender",
        "language",
        "currency",
        "busker",
    ]

    list_filter = UserAdmin.list_filter + ("busker",)
