from django.db import models

from apps.common.models import TimeStampedModel


class Role(TimeStampedModel):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_system = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "roles"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Permission(TimeStampedModel):

    module = models.CharField(
        max_length=100,
    )

    code = models.CharField(
        max_length=100,
        unique=True,
    )

    name = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "permissions"

    def __str__(self):
        return self.name
    
class RolePermission(TimeStampedModel):

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "role_permissions"

        unique_together = (
            "role",
            "permission",
        )

class SystemSetting(TimeStampedModel):

    key = models.CharField(
        max_length=100,
        unique=True,
    )

    value = models.TextField()

    description = models.TextField(
        blank=True,
    )

    class Meta:
        db_table = "system_settings"

class Holiday(TimeStampedModel):

    name = models.CharField(max_length=150)

    holiday_date = models.DateField()

    is_recurring = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "holidays"

class WorkSchedule(TimeStampedModel):

    name = models.CharField(max_length=100)

    start_time = models.TimeField()

    end_time = models.TimeField()

    break_start = models.TimeField(
        null=True,
        blank=True,
    )

    break_end = models.TimeField(
        null=True,
        blank=True,
    )

    working_hours = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    class Meta:
        db_table = "work_schedules"

class AuditLog(TimeStampedModel):

    user = models.ForeignKey(
        "identity.User",
        on_delete=models.SET_NULL,
        null=True,
    )

    action = models.CharField(
        max_length=100,
    )

    module = models.CharField(
        max_length=100,
    )

    object_id = models.CharField(
        max_length=100,
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "audit_logs"

