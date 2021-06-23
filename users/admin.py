from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomAdminUser(UserAdmin):

    """Custom User Admin Definition"""

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
                    "artist",
                    "channel",
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
        "artist",
        "channel",
    ]

    list_filter = UserAdmin.list_filter + ("artist",)
