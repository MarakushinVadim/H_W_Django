from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(
        upload_to="users/avatar/",
        **NULLABLE, verbose_name="Аватар",
        help_text="Загрузите аватар"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone",
        **NULLABLE,
        help_text="Введите номер телефона"
    )
    country = models.CharField(
        max_length=255,
        verbose_name="Country",
        **NULLABLE,
        help_text="Введите название страны"
    )
    token = models.CharField(max_length=255, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
