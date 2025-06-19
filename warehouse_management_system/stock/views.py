from django.shortcuts import render
from rest_framework import viewsets
from .models import Stack
from .serializers import StackSerializer

class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer