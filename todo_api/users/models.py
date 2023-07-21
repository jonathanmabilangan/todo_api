from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import CharField
from django.utils.translation import gettext_lazy

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    name = CharField(gettext_lazy("Name of user"), blank=True, max_length=255)
