import django_tables2 as tables

from netbox.tables import NetBoxTable
from .models import VpnConnection

class VpnConnectionListTable(NetBoxTable):
    remote_organisation = tables.Column(
        linkify=True
    )
    
    class Meta(NetBoxTable.Meta):
        model = VpnConnection
        fields = ('pk','id','vpn_endpoint',
        'remote_organisation','tenant',
        'actions')
        default_columns = ('id','remote_organisation','tenant','vpn_endpoint')

