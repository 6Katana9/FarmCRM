from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import CustomLoginSerializer, UsersSerializer

User = get_user_model()

class Login(TokenObtainPairView):
    serializer_class = CustomLoginSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
