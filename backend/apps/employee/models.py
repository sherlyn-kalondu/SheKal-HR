from django.db import models

from apps.common.models import TimeStampedModel
from apps.identity.models import User
from apps.organization.models import (
    Company,
    Branch,
    Department,
    Position,
    EmploymentType,
    JobGrade,
)


class Employee(TimeStampedModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee",
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    employment_type = models.ForeignKey(
        EmploymentType,
        on_delete=models.PROTECT,
    )

    job_grade = models.ForeignKey(
        JobGrade,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    employee_number = models.CharField(
        max_length=20,
        unique=True,
    )

    hire_date = models.DateField()

    termination_date = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "employees"

    def __str__(self):
        return f"{self.employee_number}"


from .identity_models import EmployeeIdentity
from .profile_models import EmployeeProfile
from .contact import EmployeeContact
from .emergency import EmergencyContact
from .bank import BankAccount
from .education import Education