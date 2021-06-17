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
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "artist",
                )
            },
        ),
    )

    list_display = [
        "username",
        "gender",
        "language",
        "currency",
        "artist",
    ]

    list_filter = UserAdmin.list_filter + ("artist",)
