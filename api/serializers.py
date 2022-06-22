from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import VpnConnection


class VpnConnectionSerializer(NetBoxModelSerializer):
   

    class Meta:
        model = VpnConnection
        fields = (
            'id', 'display', 
            'gegenstelle', 'comments', 'tags', 'tenant', 
            'created', 'last_updated',
        )