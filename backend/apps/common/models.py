from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created and updated timestamps.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True
