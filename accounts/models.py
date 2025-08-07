from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore

# Create your models here.
class User(AbstractUser):
    Role_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )
    role = models.CharField(max_length=10, choices=Role_CHOICES,)

    def __str__(self):
        return f"{self.username} ({self.role})"