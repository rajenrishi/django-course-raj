from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(required=False, min_value=21, default=21)

    class Meta:
        model = Employee
        fields = "__all__"
