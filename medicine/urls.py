from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import MedicineApiView
router = DefaultRouter()
router.register('', MedicineApiView)


urlpatterns = [
    path('', include(router.urls)),
]
