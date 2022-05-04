from rest_framework import serializers

from .models import Person


# class PersonSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=6)
#     age = serializers.IntegerField(required=False, min_value=10, default=10)
#
#     # Uncomment is using save method and separate Serializer and Model definitions
#     # def create(self, validated_data):
#     #     return Person.objects.create(**validated_data)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
