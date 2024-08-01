from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Career
from .serializers import CareerSerializer

class CareerView(APIView):
    def get(self, request):
        careers = Career.objects.all()
        serializer = CareerSerializer(careers, many=True)
        return Response(serializer.data)