from rest_framework import serializers
from ..models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'completed', 'career', 'created_at', 'updated_at']

    def validate_title(self, value):
        if Course.objects.filter(title=value).exists():
            raise serializers.ValidationError(f'A course with the title "{value}" already exists.')
        return value