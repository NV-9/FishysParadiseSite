from django.db import models
from django.contrib.auth.models import UserManager
import random 
import string

def random_code():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))

class FPManager(UserManager): 
    """
    Manager for Fishy's Paradise Users
    ----------------------------------
    """

    def create_discord_user(self, user_data):
        new_user: FPUser = self.create(
            dc_id = user_data['id'],
            dc_avatar = user_data['avatar'],
            dc_public_flags = user_data['public_flags'],
            dc_flags = user_data['flags'],
            dc_locale = user_data['locale'],
            dc_mfa_enabled = user_data['mfa_enabled'],
            dc_username = user_data['username'],
            dc_discriminator = user_data['discriminator'],
            email = user_data['email']
        )
        return new_user


class FPUser(models.Model):

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField()

    mc_id = models.CharField(db_column='uniqueId', max_length = 50, blank = True, default = "")
    mc_username = models.CharField(max_length = 50, blank = True, default = "")

    dc_id = models.PositiveBigIntegerField()
    dc_username = models.CharField(max_length = 50)
    dc_discriminator = models.CharField(max_length = 4)
    dc_avatar = models.CharField(max_length = 100)
    dc_public_flags = models.IntegerField()
    dc_flags = models.IntegerField()
    dc_locale = models.CharField(max_length = 100)
    dc_mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(auto_now = True)
    whitelisted = models.BooleanField(default = False)
    access_code = models.CharField(max_length=40, default=random_code)

    home_world = models.CharField(max_length = 255, blank = True, null = True)
    home_x = models.FloatField(blank = True, null = True)
    home_y = models.FloatField(blank = True, null = True)
    home_z = models.FloatField(blank = True, null = True)

    death_world = models.CharField(max_length = 255, blank = True, null = True)
    death_x = models.FloatField(blank = True, null = True)
    death_y = models.FloatField(blank = True, null = True)
    death_z = models.FloatField(blank = True, null = True)

    objects = FPManager()

    @property
    def discord_name(self):
        return f"{self.dc_username}#{self.dc_discriminator}"#

    def is_authenticated(self):
        return True 
    
    class Meta:
        db_table = 'fpusers'


