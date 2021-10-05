from django.test.client import Client

from rest_framework import status
from rest_framework.test import APITestCase


class AccountTestCase(APITestCase):

    client = Client()
    fixtures = [
        'user/fixtures/users.yaml',
        'account/fixtures/accounts.yaml'
    ]

    def test_account_user(self):
        body = {
            'user': '0390a508-dba5-4344-b77f-93e1227d42f4'
        }
        response = self.client.post('/user/0390a508-dba5-4344-b77f-93e1227d42f4/accounts/', data=body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_account_info(self):
        response = self.client.get(
            '/user/0390a508-dba5-4344-b77f-93e1227d42f4/accounts/e25736e4-b2db-4fa0-8917-86f5ec92463f/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['user'], '0390a508-dba5-4344-b77f-93e1227d42f4')

    def test_update_user_info(self):
        body = {
            'user': '479ec168-0139-45d0-b704-2bc4e5d0c4fb'
        }
        response = self.client.patch(
            '/user/0390a508-dba5-4344-b77f-93e1227d42f4/accounts/e25736e4-b2db-4fa0-8917-86f5ec92463f/', data=body)
        response = self.client.get(
            '/user/479ec168-0139-45d0-b704-2bc4e5d0c4fb/accounts/e25736e4-b2db-4fa0-8917-86f5ec92463f/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
