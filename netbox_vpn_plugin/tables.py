import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import VpnConnection

class VpnConnectionListTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = VpnConnection
        fields = ('pk', 'gegenstelle','tenant', 'comments', 'actions')
        default_columns = ('name', 'default_action')

