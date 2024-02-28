from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# Using DEFAULT user model in Django


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    
    # Personal contact data
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'