from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .models import Store, Product
from .serializer import StoreSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class StoreAPIView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self, *args, **kwargs):
        store_id = self.kwargs.get('store_id')
        product_id = self.request.query_params.get('product_id')
        return Store.objects.get_product_name(product_id, store_id)

    def get_serializer_class(self):
        return StoreSerializer

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


class ProductAPIView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        return Product.objects.filter(pk=product_id).values('name', 'description')

    def get_serializer_class(self):
        return StoreSerializer

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