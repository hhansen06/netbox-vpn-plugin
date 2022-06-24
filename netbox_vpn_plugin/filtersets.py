from .models import VpnConnection
import django_filters
from extras.filters import TagFilter


class VpnConnectionFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    tag = TagFilter()

    class Meta:
        model = VpnConnection
        fields = ['id', 'remote_organisation', 'tenant', 'vpn_endpoint']


    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(id__icontains=value)
                | Q(number__icontains=value)
                | Q(description__icontains=value)
        )
        return queryset.filter(qs_filter)
