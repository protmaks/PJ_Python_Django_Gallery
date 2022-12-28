import django_filters
from django_filters import DateTimeFromToRangeFilter, CharFilter, ChoiceFilter

from .models import Image, Country, User


class FilterImage(django_filters.FilterSet):
    # name = CharFilter(widget=django_filters.widgets.forms.TextInput(attrs={'class': 'form-control'}))
    geo_location = ChoiceFilter(widget=django_filters.widgets.forms.Select(attrs={'class': 'form-control'}), choices=Country.objects.all().values_list('id', 'name'))
    peoples = ChoiceFilter(widget=django_filters.widgets.forms.Select(attrs={'class': 'form-control'}),choices=User.objects.all().values_list('id', 'username'))
    date_posted = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Image
        fields = (
            'geo_location',
            'peoples',
            'date_posted',
        )