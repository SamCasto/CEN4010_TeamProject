from rest_framework import serializers
from .models import Book, Author, Publisher, WebsiteUser
import locale
from . import user_services

class BookSerializer(serializers.HyperlinkedModelSerializer):
    #copies_sold = serializers.IntegerField(required=False, allow_null=True)
    
    #copies_sold will be serialized and displayed with the comma separator, while still allowing None values and accepting empty input.
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     formatted_copies_sold = locale.format_string("%d", instance.copies_sold, grouping=True) if instance.copies_sold is not None else None
    #     representation['copies_sold'] = formatted_copies_sold
    #     return representation
    class Meta:
        model = Book
        fields = '__all__'

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
