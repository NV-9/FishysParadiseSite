from django.db import models
from django.contrib.auth.models import UserManager
from django.core.exceptions import PermissionDenied
import random 
import string

def random_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

class FPManager(UserManager): 
    """
    Manager for Fishy's Paradise Users
    ----------------------------------
    """

    def create_discord_user(self, user):
        new_user: FPUser = self.create(
            dc_id = user['id'],
            dc_avatar = user['avatar'],
            dc_public_flags = user['public_flags'],
            dc_flags = user['flags'],
            dc_locale = user['locale'],
            dc_mfa_enabled = user['mfa_enabled'],
            dc_username = user['username'],
            dc_discriminator = user['discriminator'],
            email = user['email']
        )
        return new_user


class FPUser(models.Model):

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(null = True)

    mc_id = models.CharField(db_column='uniqueId', max_length = 50, blank = True, null = True)
    mc_username = models.CharField(max_length = 50, blank = True, null = True)

    dc_id = models.PositiveBigIntegerField(blank = True, null = True)
    dc_username = models.CharField(max_length = 50, blank = True, null = True)
    dc_discriminator = models.CharField(max_length = 4, blank = True, null = True)
    dc_avatar = models.CharField(max_length = 100, blank = True, null = True)
    dc_public_flags = models.IntegerField(db_column = 'dc_public_flags', blank = True, null = True)
    dc_flags = models.IntegerField(blank = True, null = True)
    dc_locale = models.CharField(max_length = 100, blank = True, null = True)
    dc_mfa_enabled = models.BooleanField(blank = True, null = True)
    last_login = models.DateTimeField(auto_now = True, blank = True, null = True)
    whitelisted = models.BooleanField(default = False, blank = True, null = True)
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
    
    @property 
    def home_coords(self):
        if all([self.home_x, self.home_y, self.home_z]):
            return f"{self.home_x}, {self.home_y}, {self.home_z}"
        return "Not Set"
    
    @property 
    def death_coords(self):
        if all([self.death_x, self.death_y, self.death_z]):
            return f"{self.death_x}, {self.death_y}, {self.death_z}"
        return "Not Set"

    def is_authenticated(self):
        return True 
    
    def is_active(self):
        return False
    
    def is_staff(self):
        return False
    
    def has_module_perms(self, *args):
        return False
    
    def has_perm(self, *args):
        raise PermissionDenied 
    
    def __str__(self):
        return self.discord_name
    
    class Meta:
        db_table = 'fpusers'

