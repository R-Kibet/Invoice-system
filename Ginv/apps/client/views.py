from django.shortcuts import render
from .models import Client
from .serializer import ClientSerializer

from rest_framework import viewsets

from django.core.exceptions import PermissionDenied

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied("wrong owner")
        serializer.save()