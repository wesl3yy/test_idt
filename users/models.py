from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.conf import settings
from .manage import StoreQueryset, OrderQueryset, ListProductQueryset

User = settings.AUTH_USER_MODEL


# Create your models here.
class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'user'
        managed = True


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'category'
        managed = True


class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', related_query_name='category')

    class Meta:
        db_table = 'product'
        managed = True


class Store(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    objects = StoreQueryset.as_manager()

    class Meta:
        db_table = 'store'
        managed = True


class StoreListProduct(models.Model):
    AVAILABLE = 1
    OUT_OF_STOCK = 0
    AVAILABLE_CHOICES = (
        (AVAILABLE, 'Available'),
        (OUT_OF_STOCK, 'Out of Stock')
    )
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    is_available = models.IntegerField(choices=AVAILABLE_CHOICES, default=AVAILABLE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='list_products', related_query_name='list_product')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_products', related_query_name='store_product')

    objects = ListProductQueryset.as_manager()

    class Meta:
        db_table = 'list_product'
        managed = True


class Order(models.Model):
    quantity = models.IntegerField(null=False)
    order_date = models.DateTimeField(auto_now_add=True, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='user_stores', related_query_name='store')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='user_products', related_query_name='product')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_orders', related_query_name='user_order')

    objects = OrderQueryset.as_manager()

    class Meta:
        db_table = 'order'
        managed = True
