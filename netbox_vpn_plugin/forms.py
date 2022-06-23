from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import VpnConnection, VpnConnectionPhase2
from tenancy.models import Tenant, Contact
from dcim.models import Device

class VpnConnectionForm(NetBoxModelForm):
    comments = CommentField()

    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=True
    )
    vpn_endpoint = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=True
    )

    customer_contact = DynamicModelChoiceField(
        queryset=Contact.objects.all(),
        required=True
    )

    fieldsets = (
            ('Organizational', 
                ('remote_organisation', 'tenant', 'ordered_by','change_id','customer_contact','status')
            ),
            ('Network', 
                ('vpn_endpoint','remote_gateway_ip','nat_traversal','dead_pear_detection')
            ),
            ('Auth', 
                ('auth_method','pre_shared_key','ike_version','accept_types','accept_peer_id')
            ),
             ('Phase 1 Proposal', 
                ('encrytion','authentication','dh_group','key_lifetime','local_id')
            ), 
            )

    class Meta:
        model = VpnConnection
        exclude = []


class VpnConnectionPhase2Form(NetBoxModelForm):
    vpn_connection = DynamicModelChoiceField(
        queryset=VpnConnection.objects.all()
    )

    class Meta:
        model = VpnConnectionPhase2
        fields = (
            'vpn_connection', 'name', 'local_address', 'remote_address', 'encrytion', 'authentication',
            'dh_group', 'key_lifetime', 'tags',
        )

