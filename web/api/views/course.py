from rest_framework import generics
from rest_framework.exceptions import ValidationError
from ..models import Course
from ..serializers import CourseSerializer
from ..permissions import IsAdminOrReadOnly


class CourseListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all courses and creating a new course.
    Only admin users can create courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
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
            
        return Course.objects.filter(**status_filter[status])
    
        

class CourseDetailsView(generics.RetrieveUpdateAPIView):
    """
    Handles retrieving a specific course by its ID and updating it.
    Only admin users can update courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
    