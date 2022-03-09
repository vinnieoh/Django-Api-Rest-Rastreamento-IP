from rest_framework.test import APITestCase
from model_bakery import baker


class TestModel(APITestCase):

    def setUp(self):
        self.model = baker.make('IpModel')

    def test_str(self):

        self.assertEqual(str(self.model.query), self.model.query)
