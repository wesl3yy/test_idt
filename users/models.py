from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'user'
        managed = True


class UserStore(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users', related_query_name='user', primary_key=False)

    class Meta:
        db_table = 'user_store'
        managed = True
