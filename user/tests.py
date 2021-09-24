from django.test.client import Client

from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):

    client = Client()
    fixtures = [
        'user/fixtures/users.yaml'
    ]

    def test_create_user(self):
        body = {
            'optional_id': 'abc',
            'email': 'user@test.com'
        }
        response = self.client.post('/user/', data=body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user_info(self):
        response = self.client.get('/user/0390a508-dba5-4344-b77f-93e1227d42f4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['optional_id'], '0390a508-dba5-4344-b77f-93e1227d42f4')

    def test_update_user_info(self):
        body = {
            'email': 'user@test.com'
        }
        response = self.client.patch('/user/0390a508-dba5-4344-b77f-93e1227d42f4/', data=body)
        response = self.client.get('/user/0390a508-dba5-4344-b77f-93e1227d42f4/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'user@test.com')
