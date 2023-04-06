from rest_framework import serializers
from .models import MyUser, Store, Product, StoreListProduct


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
    description = serializers.CharField(read_only=True)

    class Meta:
        model = Store
        fields = ('name', 'description')


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(read_only=True)
    product_name = serializers.CharField(read_only=True)
    store_name = serializers.CharField(read_only=True)
    order_date = serializers.DateTimeField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ('customer_name', 'product_name', 'store_name', 'order_date', 'quantity')


class ListProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True)
    quantity = serializers.IntegerField(read_only=True)
    price = serializers.FloatField(read_only=True)
    is_available = serializers.IntegerField(read_only=True)

    class Meta:
        model = StoreListProduct
        fields = ('product_name', 'quantity', 'price', 'is_available')