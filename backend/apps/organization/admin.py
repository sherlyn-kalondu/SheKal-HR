from django.contrib import admin

from .models import (
    Company,
    Branch,
    Department,
    Position,
    EmploymentType,
    JobGrade,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "registration_number",
        "tax_pin",
        "country",
        "is_active",
    )

    search_fields = (
        "name",
        "registration_number",
        "tax_pin",
    )

    list_filter = (
        "country",
        "is_active",
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "branch_code",
        "company",
    )

    search_fields = (
        "name",
        "branch_code",
    )

    list_filter = (
        "company",
    )


# Register remaining models
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(EmploymentType)
admin.site.register(JobGrade)