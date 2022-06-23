from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import VpnConnection


class VpnConnectionSerializer(NetBoxModelSerializer):
   

    class Meta:
        model = VpnConnection
        fields = (
            'id', 'display', 
            'vpn_endpoint', 'remote_organisation', 'comments', 'tags', 'tenant', 
            'created', 'last_updated',
        )