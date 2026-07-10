from django.db import models

from apps.common.models import TimeStampedModel
from apps.employee.models import Employee


class EmergencyContact(TimeStampedModel):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="emergency_contacts",
    )

    full_name = models.CharField(max_length=150)

    relationship = models.CharField(max_length=50)

    phone_number = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.full_name
