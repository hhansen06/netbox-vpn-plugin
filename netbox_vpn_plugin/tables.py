import django_tables2 as tables

from netbox.tables import NetBoxTable
from .models import VpnConnection

class VpnConnectionListTable(NetBoxTable):
    gegenstelle = tables.Column(
        linkify=True
    )
    class Meta(NetBoxTable.Meta):
        model = VpnConnection
        fields = ('pk','id',
        'gegenstelle','tenant',
        'actions')
        default_columns = ( 'gegenstelle','tenant','id')

