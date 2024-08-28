from django.db import models
from django.utils.crypto import get_random_string


class Invitation(models.Model):
    first_invitation = models.CharField(max_length=255)
    second_invitation = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(
        max_length=10,
        choices=[
            ('accepted', 'Приду'),
            ('declined', 'Не приду'),
            ('pending', 'Ожидание')
        ],
        default='pending'
    )
    token = models.CharField(max_length=50, unique=True, blank=True)
    wish = models.TextField(verbose_name="пожелания", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(50)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Приглашение для {self.first_invitation} {self.second_invitation}"

