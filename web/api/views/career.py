from rest_framework import generics
from ..models import Career
from ..serializers import CareerSerializer
from ..permissions import IsAdminOrReadOnly

class CareerListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all careers and creating a new career.
    Only admin users can create careers.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAdminOrReadOnly]


class CareerDetailView(generics.RetrieveUpdateAPIView):
    """
    Handles retrieving a specific career by its ID and updating it.
    Only admin users can update careers.
    """
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    lookup_field = 'id'
