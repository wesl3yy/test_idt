from django.db.models import F
from django.db.models.query import QuerySet


class StoreQueryset(QuerySet):
    def get_product_name(self, store_id, product_id):
        return self.filter(
            product_id=product_id,
            pk=store_id
        ).annotate(product_name=F('product__name'))


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
        ).values('customer_name', 'product_name', 'store_name')
