from bookstore_app.models import Book, Author, Publisher, WebsiteUser, ShoppingCart, CartItem
from bookstore_app.serializers import BookSerializer, AuthorSerializer, PublisherSerializer, WebsiteUserSerializer,UpdateUserSerializer, ShoppingCartSerializer, CartItemSerializer
from rest_framework.response import Response
from rest_framework import views, response, exceptions, permissions, viewsets, status, generics
from bookstore_app import serializers as user_serializers, user_services
from bookstore_app import authentication, models
from rest_framework.permissions import IsAdminUser


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class WebsiteUserViewSet(viewsets.ModelViewSet):
    queryset = WebsiteUser.objects.all()
    serializer_class = WebsiteUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

#API endpoint that creates a user profile
class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = WebsiteUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        # Check if a user with the same username or email already exists
        if WebsiteUser.objects.filter(username=data.username).exists():
            return response.Response(data={"message": "Username already in use."}, status=status.HTTP_400_BAD_REQUEST)

        if WebsiteUser.objects.filter(email=data.email).exists():
            return response.Response(data={"message": "Email already in use."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        serializer.instance = user_services.create_user(user_dc=data)
    
        print(data)

        return response.Response(data={"User": "created"})

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAuthor(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        author = self.kwargs['author']
        books = Book.objects.filter(author__iexact=author)
        return books

#API endpoint that lets users log into their account, if they have one   
class LoginAPI(views.APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = user_services.user_username_selector(username=username)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        #Creates a token from the authentication.py file to let users log in with their credentials
        token = user_services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)
        resp.data = {"message" : "You're now logged in."}

        return resp

#Profile view endpoint    
class WebsiteUserAPI(views.APIView):

    #this endpoint is accessible only if user is authenticated

    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user

        serializer = user_serializers.WebsiteUserSerializer(user)

        return response.Response(serializer.data)



#Logout endpoint  
class LogoutAPI(views.APIView):

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "You're now logged out."}

        return resp
    

#API endpoint that allows superusers to view all website users and edit if needed.
class UserViewSet(viewsets.ModelViewSet):
    queryset = WebsiteUser.objects.all().order_by('-date_joined')
    serializer_class = WebsiteUserSerializer
    permission_classes = [IsAdminUser]

#API view that lets website users update their profile info
class UpdateProfileView(generics.UpdateAPIView):

    queryset = WebsiteUser.objects.all()
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class CreateCreditCard(views.APIView):
    queryset = models.WebsiteUser.objects.all()
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = WebsiteUserSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        credit_card_number = request.data.get("credit_card_number")

        if not credit_card_number:
            return Response({"error": "Credit card number is required."}, status=status.HTTP_400_BAD_REQUEST)

        user.credit_card_number = credit_card_number
        user.save()
        
        return response.Response(data={"Credit Card": "created"})

class CartOwnerID(generics.ListAPIView):
    serializer_class = ShoppingCartSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        try:
            user_profile = WebsiteUser.objects.get(pk=user_id)
        except WebsiteUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user_cart = ShoppingCart.objects.filter(owner=user_profile)
        return user_cart
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            message = "There is no shopping cart found for the specified user."
            return Response({'message': message})
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)