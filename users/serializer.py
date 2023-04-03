from rest_framework import serializers
from .models import User, UserStore


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], password=validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserStoreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True)
    bio = serializers.CharField(read_only=True)

    class Meta:
        model = UserStore
        fields = ('name', 'category', 'bio')
