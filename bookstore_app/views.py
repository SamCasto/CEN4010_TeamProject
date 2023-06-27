from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from bookstore_app.serializers import UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAuthor(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        books = Book.objects.filter(author__iexact=author)
        return books

class BookAuthorID(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        authorID = self.kwargs['author_id']
        return Book.objects.filter(author__id=authorID)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            # Return a custom response if there are no books
            message = "No books found for the specified author."
            return Response({'message': message})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)