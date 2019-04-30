from .models import Books
import django_filters

class BookFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model  = Books
        fields = ['tags']
