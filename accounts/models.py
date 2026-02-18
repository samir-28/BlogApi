from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        AUTHOR = "AUTHOR", "Author"
        READER = "READER", "Reader"

    role = models.CharField(max_length=10, choices=Roles.choices)

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN

    @property
    def is_author(self):
        return self.role == self.Roles.AUTHOR

    @property
    def is_reader(self):
        return self.role == self.Roles.READER

