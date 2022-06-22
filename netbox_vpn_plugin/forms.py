from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField

from .models import VpnConnection

class VpnConnectionForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = VpnConnection
        fields = ('gegenstelle', 'tenant', 'remote_ip', 'customer_contact', 'comments')
