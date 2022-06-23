from netbox.filtersets import NetBoxModelFilterSet
from .models import VpnConnection


class VpnConnectionFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = VpnConnection
        fields = ('id', 'remote_organisation', 'tenant', 'vpn_endpoint')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
