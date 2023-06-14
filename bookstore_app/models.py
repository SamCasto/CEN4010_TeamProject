from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    

class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=25)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName + self.lastName
    
class Rating(models.Model):
    rating = models.DecimalField(
        max_digits=2, decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    dateStamp = models.DateField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"Rating: {self.rating} | Book: {self.book.title} | User: {self.user.username}"

class Comment(models.Model):
    comment = models.TextField()
    dateStamp = models.DateField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment: {self.comment} | Book: {self.book.title} | User: {self.user.username}"

class Wishlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user.username} | Wishlist name: {self.name}"

class BookInWishlist(models.Model):
    wishlist = models.ForeignKey('Wishlist', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book)

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    
