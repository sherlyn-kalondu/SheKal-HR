from django.db import models

from apps.common.models import TimeStampedModel
from apps.employee.models import Employee


class BankAccount(TimeStampedModel):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="bank_accounts",
    )

    bank_name = models.CharField(max_length=150)

    branch_name = models.CharField(
        max_length=150,
        blank=True,
    )

    account_name = models.CharField(max_length=150)

    account_number = models.CharField(max_length=50)

    is_primary = models.BooleanField(default=True)

    def __str__(self):
        return self.account_name
