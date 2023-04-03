from rest_framework import generics, status
from rest_framework.response import Response

from .authentication import JWTAuthentication
from .serializer import RegisterSerializer, UserSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully",
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = UserSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     username = serializer.validated_data.get('username')
    #     password = serializer.validated_data.get('password')
    #     user = User.objects.filter(username=username, password=password).first()
    #     if not user:
    #         return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # Generate the JWT token
    #     jwt_token = JWTAuthentication.create_jwt(user)
    #
    #     return Response({'token': jwt_token})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.filter(username=username, password=password).first()

        if not user:
            return Response({'Message': 'Wrong username or password'})
        header = JWTAuthentication.get_header(request=request.META.get('HTTP_AUTHORIZATION'))
        raw_token = JWTAuthentication.get_raw_token(header)
        jwt_token = JWTAuthentication.get_validated_token(raw_token)
        return Response(jwt_token)