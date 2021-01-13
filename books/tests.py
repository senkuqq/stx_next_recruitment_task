import json

from django.test import TestCase
from rest_framework.test import APIClient
from books.google_books_client import GoogleBooksClient

# Create your tests here.
from books.models import Book


class TestGeolocation(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_google_books_client(self):
        client = GoogleBooksClient()
        response = client.get_books_by_search_param(search_param="war")
        self.assertTrue(response.status_code == 200, 'Wrong status code')

    def test_import_books(self):
        payload = {
            "q": "9785042737619" #God of war - G.Misztal, Id = XyYREAAAQBAJ
        }
        response = self.client.post('/api/v1/db/', data=json.dumps(payload), content_type='application/json')
        self.assertTrue(response.status_code == 201, 'Wrong status code')
        self.assertTrue(Book.objects.filter(google_id='XyYREAAAQBAJ').exists(), 'Book not created')
