from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import models as auth_models

class BaseUserManager(auth_models.BaseUserManager):

    def create_user(self, username: str, first_name: str, last_name: str, email: str, password: str=None, is_staff=False, is_superuser=False) -> "WebsiteUser":
        user = self.model()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.set_password(password)
        user.it_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(self, username:str, email:str, password:str=None) -> "WebsiteUser":
        user = self.create_user(
            username = username,
            first_name="",
            last_name="",
            email = email,
            password = password,
            is_staff = True,
            is_superuser = True,
        )
        user.save()

        return user

class WebsiteUser(auth_models.AbstractUser):
    username = models.CharField(verbose_name='Username', max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(verbose_name="First Name", max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True, blank=True, null=True)
    address = models.CharField(verbose_name='Home Address', max_length=255, blank=True, null=True)
    credit_card_number = models.CharField(verbose_name='Credit Card Number', max_length=16, blank=True, null=True)

    objects = BaseUserManager()


class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=255,default="")
    desc = models.TextField(default="")
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, default=1)
    genre = models.CharField(max_length=100,default="")
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, default=1)
    yearPublished = models.IntegerField(default=1900)
    copiesSold = models.IntegerField(default=0)
    # Other fields...

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=60)
    bio = models.TextField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName + self.lastName
    
class Rating(models.Model):
    rating = models.DecimalField(
        max_digits=2, decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    dateStamp = models.DateField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('WebsiteUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating: {self.rating} | Book: {self.book.title} | User: {self.user.username}"

class Comment(models.Model):
    comment = models.TextField()
    dateStamp = models.DateField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('WebsiteUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment: {self.comment} | Book: {self.book.title} | User: {self.user.username}"

class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('WebsiteUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username} | Wishlist name: {self.name}"

class BookInWishlist(models.Model):
    wishlist = models.ForeignKey('Wishlist', on_delete=models.CASCADE)
    user = models.ForeignKey('WebsiteUser', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book)

class ShoppingCart(models.Model):
    user = models.OneToOneField(WebsiteUser, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
