from rest_framework import generics
from ..models import Career
from ..serializers import CareerSerializer
from ..permissions import IsAdminOrReadOnly

class CareerListCreateView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAdminOrReadOnly]


class CareerDetailView(generics.RetrieveUpdateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    lookup_field = 'id'
