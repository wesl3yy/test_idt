from django.db.models import F
from django.db.models.query import QuerySet


class StoreQueryset(QuerySet):
    def get_product_name(self, store_id, product_id):
        return self.filter(
            product_id=product_id,
            pk=store_id
        ).annotate(product_name=F('product__name'))
