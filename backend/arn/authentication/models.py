from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class ArnUser(AbstractUser):
    # Idk, not using any of these fields yet really
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    email = models.CharField(max_length=120)
