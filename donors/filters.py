import django_filters

from .models import Donors


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Donors
        fields = '__all__'
        exclude = ['quantity', 'date_of_payment', 'recipient']
