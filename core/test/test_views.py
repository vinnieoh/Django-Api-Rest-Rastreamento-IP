from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

from core.models import IpModel


class TestViews(APITestCase):
    
    def setUp(self):
        self.ip_valido = {'ip':'148.45.56.73'}
        self.ip_invalido = {'ip':'243.172.240.104'}
        self.client = APIClient()


    def test_create_ip_valido(self):
        
        url = reverse('ip')
        re = self.client.post(url, self.ip_valido, format='json')

        self.assertEqual(re.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IpModel.objects.count(), 1)

    def test_create_ip_invalido(self):

        url = reverse('ip')
        res = self.client.post(url, self.ip_invalido, format='json')

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_lista_todos_os_ips(self):

        url = reverse('ips')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)