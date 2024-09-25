from rest_framework import generics
from rest_framework.exceptions import ValidationError
from ..models import Topic
from ..serializers import TopicSerializer
from ..permissions import IsAdminOrReadOnly

class TopicListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all topics and creating a new topic.
    Only admin users can create topics.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        query_params = self.request.query_params
        
        invalid_params = set(query_params.keys()) - {'status'}
        if invalid_params:
            raise ValidationError(f"Invalid query parameter(s): {', '.join(query_params)}. Only 'status' is allowed") 
        
        status = query_params.get('status')
        
        status_filter = {
            None: {'completed': True},
            'completed': {'completed': True},
            'incomplete': {'completed': False},
            'all': {},
        }
        
        if status not in status_filter:
            raise ValidationError(f"Invalid value for 'status': {status}. Valid options are 'completed', 'incomplete', or 'all'.")
            
        return Topic.objects.filter(**status_filter[status])


class TopicDetailsView(generics.RetrieveUpdateAPIView):
    """
    Handles retrieving a specific topic by its ID and updating it.
    Only admin users can update topics.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'
    
    def action(self):
        if self.request.user.is_staff:
            serializer.save()
    