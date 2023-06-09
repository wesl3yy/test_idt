from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from .filters import StoreAPIFilterSet, OrderAPIFilterSet
from .models import Store, Order, StoreListProduct
from .serializer import StoreSerializer, OrderSerializer, ListProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils import get_access


class StoreAPIView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    filterset_class = StoreAPIFilterSet

    def get_queryset(self, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        store_id = self.request.query_params.get('store_id')
        return Store.objects.get_product_name(store_id, user_id)

    def get_serializer_class(self):
        return StoreSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        header = get_access(self, request=request)
        if header:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=200)
        return Response({'message': 'Permission denied'})


class OrderAPIView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    filterset_class = OrderAPIFilterSet

    def get_queryset(self, *args, **kwargs):
        order_id = self.kwargs.get('order_id')
        user_id = self.request.query_params.get('user_id')
        store_id = self.request.query_params.get('store_id')
        product_id = self.request.query_params.get('product_id')
        return Order.objects.get_order_detail(order_id, user_id, store_id, product_id)

    def get_serializer_class(self):
        return OrderSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        header = get_access(self, request=request)
        if header:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=200)
        return Response({'message': 'Permission denied'})


class ListProductAPIView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self, *args, **kwargs):
        store_id = self.kwargs.get('store_id')
        product_id = self.request.query_params.get('product_id')
        if product_id:
            return StoreListProduct.objects.get_product(store_id, product_id)
        return StoreListProduct.objects.get_all_product(store_id)

    def get_serializer_class(self):
        return ListProductSerializer

    @action(detail=True, methods=['get'])
    def get(self, request, *args, **kwargs):
        header = get_access(self, request=request)
        if header:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=200)
        return Response({'message': 'Permission denied'})
