from rest_framework import viewsets
from .models import Hotel
from .serializers import HotelSerializer
from django.db.models import Q


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Initialize an empty Q object
        filters = Q()

        # Perform custom filtering based on your requirements
        is_active = self.request.query_params.get("is_active", None)
        query = self.request.query_params.get("query", None)

        if is_active:
            filters &= Q(is_active=True)

        if query:
            filters &= Q(name__icontains=query)

        queryset = queryset.filter(filters)
        return queryset
