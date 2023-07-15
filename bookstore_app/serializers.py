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
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    email = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    address = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    credit_card_number = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    
    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return user_services.UserDataClass(**data)
    
#serializer that takes care of updating user info    
class UpdateUserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(read_only=True, required = False)

    class Meta:
        model = WebsiteUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'credit_card_number')
        extra_kwargs = {
            'username' : {'required' : False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'address': {'required': False},
            'credit_card_number': {'required': False}
        }
        
    #check to see if the updated username is already taken
    def validate_username(self, value):
        user = self.context['request'].user
        if WebsiteUser.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        #The primary id for the website user needs to match, otherwise you cannot update it
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You don't have permission for this user."})

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.address = validated_data.get('address', instance.address)
        instance.credit_card_number = validated_data.get('credit_card_number', instance.credit_card_number)

        instance.save()

        return instance