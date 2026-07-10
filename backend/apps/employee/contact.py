from django.db import models

from apps.common.models import TimeStampedModel
from apps.employee.models import Employee


class EmployeeContact(TimeStampedModel):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="contact",
    )

    phone_number = models.CharField(max_length=20)

    alternative_phone = models.CharField(
        max_length=20,
        blank=True,
    )

    personal_email = models.EmailField()

    work_email = models.EmailField(
        blank=True,
    )

    county = models.CharField(max_length=100)

    constituency = models.CharField(
        max_length=100,
        blank=True,
    )

    ward = models.CharField(
        max_length=100,
        blank=True,
    )

    postal_address = models.CharField(
        max_length=200,
        blank=True,
    )

    physical_address = models.TextField()

    def __str__(self):
        return self.employee.employee_number
