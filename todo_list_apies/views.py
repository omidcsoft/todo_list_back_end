from .models import ToDo
from .serializers import ToDoSerializer,TokenModelSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView,ListCreateAPIView

class ToDoViewSet(viewsets.ModelViewSet):
    
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['token']

    def get_queryset(self):
        return ToDo.objects.filter(is_active=True).select_related('user')










