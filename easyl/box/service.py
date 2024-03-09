from django_filters import rest_framework as filters
from .models import *



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UserBoxFilter(filters.FilterSet):
    user = CharFilterInFilter(field_name='user__name', lookup_expr='in')
    

    class Meta:
        model = Box
        fields = ['user']