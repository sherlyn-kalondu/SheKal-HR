from django.db import models

from apps.common.models import TimeStampedModel
from apps.employee.models import Employee


class Education(TimeStampedModel):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="education",
    )

    institution = models.CharField(max_length=200)

    qualification = models.CharField(max_length=200)

    field_of_study = models.CharField(max_length=200)

    start_date = models.DateField()

    end_date = models.DateField()

    grade = models.CharField(
        max_length=50,
        blank=True,
    )

    def __str__(self):
        return self.qualification
