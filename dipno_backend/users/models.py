from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    facebook_id = CharField(max_length=200, unique=True)
    profile_image = CharField(max_length=300, blank=True)
    gender = CharField(max_length=10, blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    Token.objects.get_or_create(user=instance)
