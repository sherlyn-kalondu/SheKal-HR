from django.db import models

from apps.common.models import TimeStampedModel
from apps.employee.models import Employee


class EmployeeProfile(TimeStampedModel):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    first_name = models.CharField(max_length=100)

    middle_name = models.CharField(
        max_length=100,
        blank=True,
    )

    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=20)

    date_of_birth = models.DateField()

    marital_status = models.CharField(
        max_length=30,
        blank=True,
    )

    nationality = models.CharField(
        max_length=100,
        default="Kenyan",
    )

    photo = models.ImageField(
        upload_to="employees/photos/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"