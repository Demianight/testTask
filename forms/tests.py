from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class NewsTestCase(APITestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('form-list') + 'get_form/'

    def test_forms(self):
        '''
        IT'S SOOO BAD
        But I didn't figure out the way to fix it. So here is the problem:
        Every time when the new "def" is called every single form
        Loses its relation with field
        And therefore always returns somethingElse as the response
        I think that it's related with djongo module, I never had same problems
        With relational databases
        Hope You got me))

        P.S. Thus it's impossible to read this test here is the explanation:
        It makes requests for each type of form and checks if the answer
        Is the correct form.name
        Also it check all the validators
        '''
        post_data = {
            "email": "kdemian@yandex.ru",
            "date": "2023-15-11",
            "text": "oqainfgq",
            "phone": "+7 900 000 00 00"
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'signUp')

        post_data = {
            'email': 'admin@admin.admin',
            'phone': '+7 900 000 00 00'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'login')

        post_data = {
            'date': '2023-15-11'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'somethingElse')

        post_data = {
            'date': '2023-15-11',
            'email': 'kdemian@yandex.ru'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'lastLogin')

        post_data = {
            'email': 'kdemian@yandex.ru',
            'date': '2023-15-11',
            'text': 'oqainfgq'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'lastLogin')

        post_data = {
            'email': 'admin@admin.admin',
            'phone': '+7 900 000 00 00',
            'text': 'qwoifgnq',
            'date': '0000d-00-00'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        post_data = {
            'email': 'admin@admin.admin',
            'phone': '7 900 000 00 00',
            'text': 'qwoifgnq',
            'date': '0000-00-00'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        post_data = {
            'email': 'admin@admin@admin.admin',
            'phone': '+7 900 000 00 00',
            'text': 'qwoifgnq',
            'date': '0000d-00-00'
        }
        response = self.client.post(self.url, data=post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
