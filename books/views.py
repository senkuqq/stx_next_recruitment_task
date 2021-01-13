from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, views, status
from rest_framework.response import Response

from books.google_books_client import GoogleBooksClient
from books.models import Book, Author
from rest_framework import viewsets
from books.serializers import BookSerializer, DatabaseSerializer
from rest_framework.decorators import api_view
# Create your views here.


class AuthorSearchFilter(filters.SearchFilter):
    search_param = "author"


class BooksViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows books to be viewed, created or deleted.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, AuthorSearchFilter]
    ordering_fields = ['published_date']
    filterset_fields = ['published_date']
    search_fields = ['authors__name']


class DbView(views.APIView):
    def post(self, request):
        client = GoogleBooksClient()
        serializer = DatabaseSerializer(data=request.data)
        if serializer.is_valid():
            books = client.get_books_by_search_param(search_param=request.data.get('q'))
            if books.status_code == 200 and books.json().get('totalItems') > 0:
                id_list = []
                for book in books.json().get('items'):
                    volume_info = book.get('volumeInfo')
                    image_links = volume_info.get('imageLinks')
                    thumbnail = None
                    if image_links:
                        thumbnail = image_links.get('thumbnail')
                    book_db, book_db_created = Book.objects.update_or_create(
                        google_id=book.get('id'), defaults={
                            'title': volume_info.get('title'),
                            'published_date': volume_info.get('publishedDate'),
                            'average_rating': volume_info.get('averageRating'),
                            'ratings_count': volume_info.get('ratingsCount'),
                            'thumbnail': thumbnail,
                        }
                    )
                    authors_api = volume_info.get('authors')
                    categories_api = volume_info.get('categories')
                    if authors_api:
                        book_db.authors.clear()
                        for author_api in authors_api:
                            book_db.authors.get_or_create(name=author_api)
                    if categories_api:
                        book_db.categories.clear()
                        for category_api in categories_api:
                            book_db.categories.get_or_create(name=category_api)
                    id_list.append(book_db.id)
                queryset = Book.objects.filter(id__in=id_list)
                bs = BookSerializer(instance=queryset, many=True)
                return Response(data=bs.data, status=status.HTTP_201_CREATED)
            else:
                raise Http404
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)