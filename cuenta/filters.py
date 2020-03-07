import django_filters
from django_filters import DateFilter, CharFilter
from cuenta.models import Orden


class OrdenFilter(django_filters.FilterSet):
    fechaInicio = DateFilter(field_name="fechaCreacion", lookup_expr='gte')
    fechaFin = DateFilter(field_name="fechaCreacion", lookup_expr='lte')
    nota = CharFilter(field_name='nota', lookup_expr='icontains')

    class Meta:
        model = Orden
        fields = '__all__'
        exclude = ['cliente', 'fechaCreacion']
