from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TimeField, BigIntegerField, TextField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)

    available_from = TimeField(null=True, blank=True)
    available_to = TimeField(null=True, blank=True)

    facebook_id = BigIntegerField(null=True, blank=True)
    facebook_username = CharField(max_length=32, null=True, blank=True)
    facebook_link = CharField(max_length=256, null=True, blank=True)

    interests = TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    Token.objects.get_or_create(user=instance)
