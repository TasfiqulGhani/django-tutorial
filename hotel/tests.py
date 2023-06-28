from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Hotel
from .api import HotelViewSet
from faker import Faker


class HotelViewSetTestCase(TestCase):
    def setUp(self):
        """
        APIRequestFactory is a class provided by the Django REST Framework (DRF) that allows you to create mock API requests in your tests.
        It is used to generate request objects that simulate incoming requests to your API endpoints.
        """
        self.factory = APIRequestFactory()
        self.view = HotelViewSet.as_view({"get": "list"})
        self.url = "/"
        self.faker = Faker()

        # Create some sample hotels for testing
        self.hotel1 = Hotel.objects.create(
            name="Hotel A", is_active=True, description="Hotel A description"
        )
        self.hotel2 = Hotel.objects.create(
            name="Hotel B", is_active=False, description="Hotel B description"
        )

    def test_get_queryset(self):
        # Test filtering active hotels only
        request = self.factory.get(self.url, {"is_active": "true"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.data), 1
        )  # Only one active hotel should be returned

        # Test retrieving all hotels
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Both hotels should be returned

    def test_search_queryset(self):
        # Test filtering active hotels only
        self.hotel3 = Hotel.objects.create(
            name="Hotel A", is_active=False, description="Hotel A description"
        )

        request = self.factory.get(self.url, {"is_active": "true", "query": "Hotel A"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.data), 1
        )  # Only one active hotel should be returned

        # Test retrieving all hotels
        request = self.factory.get(self.url, {"query": "Hotel A"})
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # Both hotels should be returned
