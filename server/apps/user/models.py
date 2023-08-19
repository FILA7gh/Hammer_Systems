import random
import string
from django.db import models


class CustomUser(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    activated_code = models.CharField(max_length=6, null=True, blank=True, unique=True)
    activated_by = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='activated_users')
    is_activated = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'id {self.id}: {self.phone_number}'

    @staticmethod
    def generate_random_code():

        """ Генерация рандомного 6-значного кода из цифр и символов """

        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))


class InvitationCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id}'
