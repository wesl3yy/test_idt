from rest_framework import generics
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from rest_framework.decorators import action


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
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        username = self.request.query_params.get('username')
        password = self.request.query_params.get('password')
        return User.objects.filter(username=username, password=password)

    def get_serializer_class(self):
        return UserSerializer

    @action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset)
        return Response(serializer.data())
