from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = "Create user :"

    def handle(self, *args, **kwargs):
        username = input("Username: ")
        password = input("Password: ")
        role = input("Role: ")

        user = User.objects.create_user(
            username=username,
            password=password,
            role=role
        )

        self.stdout.write(self.style.SUCCESS("User created successfully"))
