from django.contrib.auth.models import AbstractUser
from django.db import models
import channels
from studios import models as studio_models
from channels import models as channel_models


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "other"),
    ]

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"
    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    ]

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    ]

    avatar = models.ImageField(blank=True)
    nickname = models.CharField(max_length=80, blank=True, null=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, blank=True, null=True
    )
    birthdate = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        blank=True,
        null=True,
        default=LANGUAGE_KOREAN,
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        blank=True,
        null=True,
        default=CURRENCY_KRW,
    )
    busker = models.BooleanField(default=False)
