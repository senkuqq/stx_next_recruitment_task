import requests
import json
from django.conf import settings

DOMAIN = 'https://www.googleapis.com/books/v1/'


class GoogleBooksClient():
    def get_books_by_search_param(self, search_param):
        response = requests.get('{}volumes?q={}'.format(DOMAIN, search_param))
        return response


