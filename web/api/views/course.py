from rest_framework import generics
from rest_framework.exceptions import ValidationError
from ..models import Course
from ..serializers import CourseSerializer
from ..permissions import IsAdminOrReadOnly


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        
        query_filter = {
            None: {'completed': True},
            'completed': {'completed': True},
            'incomplete': {'completed': False},
            'all': {},
        }
        
        if query not in query_filter:
            raise ValidationError(f"Invalid query parameter: {query}. Valid options are 'completed', 'incomplete', or 'all.")
            
        return Course.objects.filter(**query_filter[query])
    
        

class CourseDetailsView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
    