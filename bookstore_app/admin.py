from django.contrib import admin
from .models import Book, Author, Publisher, WebsiteUser, ShoppingCart, CartItem

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(WebsiteUser)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)