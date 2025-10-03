from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'photo', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_photo(self, value):

        if not value:
            return value
        max_size = 5 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError("Photo file size must be <= 5 MB.")
        content_type = getattr(value, 'content_type', None)
        if content_type and not content_type.startswith('image'):
            raise serializers.ValidationError("Uploaded file must be an image.")
        return value
