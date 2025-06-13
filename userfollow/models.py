from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)
    
    def __str__(self):
        return self.user.username