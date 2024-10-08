from rest_framework import serializers
from ..models import Career

class CareerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Career model. Handles validation and ensures
    that titles are unique.
    """
    class Meta:
        model = Career
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        
    def validate_title(self, value):
        if Career.objects.filter(title=value).exists():
            serializers.ValidationError('A career with this title already exists.')
        return value
