from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # Use email as the unique identifier for registration and login
    email = models.EmailField(unique=True)

    timezone = models.CharField(
        max_length=50,
        default='America/New_York'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Remove username field as it's not needed when using email for authentication
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
