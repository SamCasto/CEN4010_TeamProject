from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from bookstore_app import views
from urllib.parse import quote

router = routers.DefaultRouter()
router.register(r'publishers', views.PublisherViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    #path('author/<int:author_id>/books/', views.BookAuthorID.as_view(), name='books_by_author'),
    path('bookstore/', include('bookstore_app.urls')),
    path('books/<str:genre>/', views.BookListByGenreView.as_view(), name='book_list_by_genre'),
    path('top-books/', views.TopBooksListView.as_view(), name='top_books'),
    path('books/rating/<str:rating>/', views.BookListByRatingView.as_view(), name='books_by_rating'),
    path('publisher-books/<str:publisher_name>/', views.PublisherBooksListView.as_view(), name='publisher_books'),
    path('publisher-books/{}/'.format(quote('Faber & Faber')), views.PublisherBooksListView.as_view(), name='publisher_books_faber'),
    path('publisher-books/{}/'.format(quote('Simon & Schuster')), views.PublisherBooksListView.as_view(), name='publisher_books_simon'),
]