from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    product_sold = models.TextField(null=True, blank=True)
    product_info = models.TextField(null=True, blank=True)