from rest_framework.serializers import ModelSerializer, ValidationError
from ..models import Topic


class TopicSerializer(ModelSerializer):
    """
    Serializer for the Course model. Handles validation and ensures
    that topics belong to a course.
    """
    class Meta:
        model = Topic
        fields = ['id', 'title', 'summary', 'completed', 'course', 'parent', 'created_at', 'updated_at']

    def validate(self, data):
        parent = data.get('parent')
        course = data.get('course')
        
        if parent and parent.course != course:
            raise ValidationError('The parent topic must belong to the same course.')
          
        return data
