from rest_framework import serializers
from main.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name_user', 'name', 'last_name', 'email')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'product')

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)
    class Meta:
        model = Product
        extra_kwargs = {'images': {'required': 'False'}}
        #fields = ('name', 'price', 'price_public', 'existence', 'category', 'description', 'code', 'images')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

