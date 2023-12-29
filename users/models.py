from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('Teacher', 'Викладач'),
        ('Student', 'Учень')
    ]
    role = models.CharField(max_length=15, choices=role_choices)

    def __str__(self):
        return self.user.username