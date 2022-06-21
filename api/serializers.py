from rest_framework import serializers

from ipam.api.serializers import NestedPrefixSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Vpn


class VpnSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vpn-api:vpn-list-detail'
    )
    rule_count = serializers.IntegerField(read_only=True)