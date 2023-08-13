from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Medicine
from .serializers import MedicineSerializer


class MedicineApiView(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

