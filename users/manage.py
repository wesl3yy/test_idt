from django.db.models import F
from django.db.models.query import QuerySet


class StoreQueryset(QuerySet):
    def get_product_name(self, store_id, user_id):
        return self.filter(
            user_id=user_id,
            pk=store_id
        ).values('name', 'description')


class OrderQueryset(QuerySet):
    def get_order_detail(self, order_id, user_id, product_id, store_id):
        return self.annotate(
            customer_name=F('user__username'),
            product_name=F('product__name'),
            store_name=F('store__name')
        ).filter(
            pk=order_id,
            user_id=user_id,
            product_id=product_id,
            store_id=store_id
        ).values('customer_name', 'product_name', 'store_name', 'order_date', 'quantity')


class ListProductQueryset(QuerySet):
    def get_product(self, store_id, product_id):
        return self.filter(
            store_id=store_id,
            product_id=product_id
        ).annotate(
            product_name=F('product__name')
        ).values('product_name', 'quantity', 'price', 'is_available')

    def get_all_product(self, store_id):
        return self.filter(
            store_id=store_id
        ).annotate(
            product_name=F('product__name')
        ).values('product_name', 'quantity', 'price', 'is_available')
