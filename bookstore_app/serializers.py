from rest_framework import serializers
from .models import Book, Author, Publisher, WebsiteUser, Rating
import locale
from . import user_services

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating', 'dateStamp', 'user')

class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    rating = RatingSerializer(many=True, read_only = True)
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebsiteUser
        fields = '__all__'
        model = Publisher
        fields = '__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class WebsiteUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    credit_card_number = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return user_services.UserDataClass(**data)
    


