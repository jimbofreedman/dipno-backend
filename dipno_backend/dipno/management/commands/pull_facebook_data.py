from django.core.management.base import BaseCommand, CommandError
from social_django.models import UserSocialAuth

import json
import facebook

class Command(BaseCommand):
    help = 'Updates user information from Facebook'

    def handle(self, *args, **options):
        for user_social in UserSocialAuth.objects.all():
            user = user_social.user
            facebook_token = user_social.extra_data["access_token"]
            graph = facebook.GraphAPI(access_token=facebook_token, version="2.12")
            data = graph.get_object(id='me', fields='id,name,link')
            user.facebook_id = data['id']
            user.facebook_link = data['link']
            user.save()
            self.stdout.write(self.style.SUCCESS('Updated "%s"' % user.username))
