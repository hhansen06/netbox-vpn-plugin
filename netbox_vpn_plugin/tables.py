import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import Vpn

class VpnListTable(NetBoxTable):

    class Meta(NetBoxTable.Meta):
        model = Vpn
        fields = ('pk', 'gegenstelle','tenant', 'comments', 'actions')
        default_columns = ('name', 'default_action')

