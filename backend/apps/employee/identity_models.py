from django.db import models

from apps.common.models import TimeStampedModel
from apps.employee.models import Employee


class EmployeeIdentity(TimeStampedModel):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="identity",
    )

    national_id = models.CharField(
        max_length=20,
        unique=True,
    )

    kra_pin = models.CharField(
        max_length=20,
        blank=True,
    )

    nssf_number = models.CharField(
        max_length=30,
        blank=True,
    )

    sha_number = models.CharField(
        max_length=30,
        blank=True,
    )

    passport_number = models.CharField(
        max_length=30,
        blank=True,
    )