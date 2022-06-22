from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import Vpn

class VpnForm(NetBoxModelForm):
    comments = CommentField()
    class Meta:
        model = Vpn
        fields = ('gegenstelle','orginator', 'tenant', 'remote_ip', 'customer_contact', 'comments')
