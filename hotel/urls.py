from django.urls import path, include
from rest_framework import routers
from .api import HotelViewSet

router = routers.DefaultRouter()
router.register(r"", HotelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
