from django.db import models

from dipno_backend.users.models import User


class Match(models.Model):
    user1 = models.ForeignKey(User, related_name="match_set1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name="match_set2", on_delete=models.CASCADE)

    accepted = models.BooleanField(default=False)

    suggested_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)

