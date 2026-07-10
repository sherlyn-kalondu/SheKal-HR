from rest_framework import serializers

from apps.employee.models import (
    BankAccount,
    Education,
    EmergencyContact,
    Employee,
    EmployeeContact,
    EmployeeIdentity,
    EmployeeProfile,
)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = "__all__"


class EmployeeIdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeIdentity
        fields = "__all__"


class EmployeeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeContact
        fields = "__all__"


class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
