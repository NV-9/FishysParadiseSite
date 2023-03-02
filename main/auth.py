from django.contrib.auth.backends import BaseBackend
from .models import FPUser

class DiscordAuthenticationBackend(BaseBackend):

    def authenticate(self, request, user) -> FPUser:
        user_data = user
        user = FPUser.objects.filter(dc_id = user_data['id'])
        if len(user) == 0:
            return FPUser.objects.create_discord_user(user_data)
        return list(user).pop()

    def get_user(self, user_id):
        try:
            return FPUser.objects.get(pk = user_id)
        except:
            return None

