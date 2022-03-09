from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestUrls(APITestCase):

    def setUp(self):
        self. client = APIClient()

    def test_creacao_ip(self):

        data = {'ip':'148.45.56.73'}
        url = reverse('ip')
        res = self.client.post(url, data=data, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        
    def test_lista_todos_ip(self):

        url = reverse('ips')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)