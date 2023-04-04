from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .filters import UserStoreFilterSet
from .models import UserStore
from .serializer import UserStoreSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserStoreAPIView(generics.GenericAPIView):
    filterset_class = UserStoreFilterSet
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        return UserStore.objects.filter(user_id=user_id).values('name', 'category', 'bio')

    def get_serializer_class(self):
        return UserStoreSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        header = JWTAuthentication.get_header(self, request=request)
        if header:
            raw_token = JWTAuthentication.get_raw_token(self, header)
            valid_token = JWTAuthentication.get_validated_token(self, raw_token)
            if valid_token:
                queryset = self.filter_queryset(self.get_queryset())
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data, status=200)
        return Response({'message': 'Permission denied'})
