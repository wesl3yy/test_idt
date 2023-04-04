import django_filters
from django_filters import filters
from .models import UserStore


class UserStoreFilterSet(django_filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='iexact')
    category = filters.CharFilter(field_name='category', lookup_expr='iexact')
    bio = filters.CharFilter(field_name='bio', lookup_expr='iexact')

    class Meta:
        model = UserStore
        fields = ('name', 'category', 'bio',)