from rest_framework import generics, status
from rest_framework.response import Response

from .authentication import JWTAuthentication as jwt
from .serializer import RegisterSerializer, UserSerializer
from .models import MyUser
from rest_framework_simplejwt.authentication import JWTAuthentication


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = (JWTAuthentication,)

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

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = MyUser.objects.filter(username=username, password=password).first()
        if not user:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the JWT token
        jwt_token = jwt.create_jwt(user)

        return Response({'token': jwt_token})
