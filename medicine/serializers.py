from rest_framework import serializers
from django.contrib.auth import get_user_model


from .models import Medicine


User = get_user_model()

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
