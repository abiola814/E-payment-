from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=2000, blank=True)
    email = models.EmailField(max_length=2000, blank=True, null=True, unique=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to = "profiles/", default = 'profiles/user-default.png')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_name)