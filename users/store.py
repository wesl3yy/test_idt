from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .filters import UserStoreFilterSet
from .models import UserStore
from .serializer import UserStoreSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserStoreAPIView(generics.GenericAPIView):
    filterset_class = UserStoreFilterSet

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        return UserStore.objects.filter(user_id=user_id).values('name', 'category', 'bio')

    def get_serializer_class(self):
        return UserStoreSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)
