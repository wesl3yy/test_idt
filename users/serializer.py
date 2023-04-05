from rest_framework import serializers
from .models import MyUser, Store, Product


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'password',)

    def create(self, validated_data):
        user = MyUser.objects.create(username=validated_data['username'], password=validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class StoreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    product_name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Store
        fields = ('name', 'product_name', 'description')


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    type = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    price = serializers.FloatField(read_only=True)
    is_available = serializers.IntegerField(read_only=True)
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
