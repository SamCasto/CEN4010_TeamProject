from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bookstore_app import views

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
    path('books/<str:id>/', views.BookDetail.as_view(), name='book-detail'),
    path('author/<int:author_id>/books/', views.BookAuthor.as_view(), name='books_by_author'),
    path('bookstore/', include('bookstore_app.urls')),
]
