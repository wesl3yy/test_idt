from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.conf import settings
from .manage import StoreQueryset

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


class Product(models.Model):
    AVAILABLE = 1
    OUT_OF_STOCK = 0
    AVAILABLE_CHOICES = (
        (AVAILABLE, 'Available'),
        (OUT_OF_STOCK, 'Out of Stock')
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    is_available = models.IntegerField(choices=AVAILABLE_CHOICES, default=AVAILABLE)
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'product'
        managed = True


class Store(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products',
                                related_query_name='product')

    objects = StoreQueryset.as_manager()

    class Meta:
        db_table = 'store'
        managed = True
