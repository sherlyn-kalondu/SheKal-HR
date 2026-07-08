from django.db import models

from apps.common.models import BaseModel


class Company(BaseModel):
    """
    Represents a company using the HR system.
    """

    name = models.CharField(
        max_length=200,
        unique=True,
    )

    registration_number = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
    )

    tax_pin = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    address = models.TextField(
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    country = models.CharField(
        max_length=100,
        default="Kenya",
    )

    logo = models.ImageField(
        upload_to="company/logos/",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "companies"
        ordering = ["name"]
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Branch(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="branches",
    )

    name = models.CharField(max_length=150)

    branch_code = models.CharField(
        max_length=20,
        unique=True,
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    address = models.TextField(
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "branches"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Department(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="departments",
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="departments",
        null=True,
        blank=True,
    )

    name = models.CharField(max_length=150)

    department_code = models.CharField(
        max_length=20,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "departments"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Position(BaseModel):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="positions",
    )

    title = models.CharField(max_length=150)

    position_code = models.CharField(
        max_length=20,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "positions"
        ordering = ["title"]

    def __str__(self):
        return self.title


class EmploymentType(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "employment_types"

    def __str__(self):
        return self.name


class JobGrade(BaseModel):
    grade = models.CharField(
        max_length=20,
        unique=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "job_grades"

    def __str__(self):
        return self.grade