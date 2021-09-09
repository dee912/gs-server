from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Shoe, Size, Category

User = get_user_model()

#! Serializers allow complex data to be converted to native Python datatypes 
#! that can then be easily rendered into JSON, XML or other content types
#! ModelSerializer class which provides a useful shortcut for creating 
#! serializers that deal with model instances and querysets.

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id')

class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'

class PopulatedShoeSerializer(ShoeSerializer):
    category = CategorySerializer(many=True)
    size = SizeSerializer(many=True)
    favourited_by = UserSerializer(many=True)
