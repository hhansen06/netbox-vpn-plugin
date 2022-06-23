from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import VpnConnection, VpnConnectionPhase2


class VpnConnectionSerializer(NetBoxModelSerializer):
    class Meta:
        model = VpnConnection
        fields = (
            'id', 'display', 
            'vpn_endpoint', 'remote_organisation', 'comments', 'tags', 'tenant', 
            'created', 'last_updated',
        )

class VpnConnectionPhase2Serializer(NetBoxModelSerializer):
    class Meta:
        model = VpnConnectionPhase2
        fields = (
            'id', 'display', 
            'vpn_connection', 'name', 'local_address', 'remote_address', 'encrytion', 'authentication', 'dh_group', 'key_lifetime', 
            'created', 'last_updated',
        )