import json
from rest_framework import status
from django.test import TestCase, Client
from core.views import ReporterViewSet, ArticleViewSet
from rest_framework.test import APIRequestFactory

client = Client()
factory = APIRequestFactory()
reporter_create = ReporterViewSet.as_view({'post': 'create'})
reporter_detail = ReporterViewSet.as_view({'get': 'retrieve'})


class CreateReporterTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'first_name': 'Jhon',
            'last_name': 'Doe',
            'email': 'teste@mail.com'
        }
        self.invalid_payload = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'teste@mail.com'
        }

    def test_create_valid_reporter(self):
        request = factory.post('/reporters/', json.dumps(self.valid_payload), content_type='application/json')
        response = reporter_create(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_reporter(self):
        request = factory.post('/reporters/', json.dumps(self.invalid_payload), content_type='application/json')
        response = reporter_create(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)