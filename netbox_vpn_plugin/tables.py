import django_tables2 as tables
from netbox.tables import NetBoxTable

from .models import VpnConnection, VpnConnectionPhase2

class VpnConnectionListTable(NetBoxTable):
    remote_organisation = tables.Column(
        linkify=True
    )
    
    class Meta(NetBoxTable.Meta):
        model = VpnConnection
        extra_controls = ('add')
        fields = (
            'pk','id',
            'remote_gateway_ip','vpn_endpoint','remote_organisation','tenant','status',
            'actions'
        )


class VpnConnectionPhase2Table(NetBoxTable):
    vpn_connection = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        empty_text = "No Phase 2 Configuration for this vpn defined"
        model = VpnConnectionPhase2
        fields = ('pk','id',
        'name','local_address','remote_address')
        default_columns = ('id','name','local_address','remote_address')
