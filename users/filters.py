import django_filters
from django_filters import filters

from .models import MyUser, Store, Product, Order, StoreListProduct


class StoreAPIFilterSet(django_filters.FilterSet):
    user_id = filters.NumberFilter(field_name='user_id', lookup_expr='exact')

    class Meta:
        model = Store
        fields = ('user_id',)

class OrderAPIFilterSet(django_filters.FilterSet):
    order_id = filters.NumberFilter(field_name='order_id', lookup_expr='exact')
    user_id = filters.NumberFilter(field_name='user_id', lookup_expr='exact')
    store_id = filters.NumberFilter(field_name='store_id', lookup_expr='exact')
    product_id = filters.NumberFilter(field_name='product_id', lookup_expr='exact')

    class Meta:
        model = Order
        fields = ('order_id', 'user_id', 'store_id', 'product_id',)


class ListProductAPIFilterSet(django_filters.FilterSet):
    store_id = filters.NumberFilter(field_name='store_id', lookup_expr='exact')
    product_id = filters.NumberFilter(field_name='product_id', lookup_expr='exact')

    class Meta:
        model = StoreListProduct
        fields = ('store_id', 'product_id',)

