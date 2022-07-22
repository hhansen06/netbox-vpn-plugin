from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import VpnConnection, VpnConnectionPhase2


class VpnConnectionSerializer(NetBoxModelSerializer):
    class Meta:
        model = VpnConnection
        fields = (
            'id', 'display', 
            'remote_organisation','vpn_endpoint', 'customer_contact', 'comments', 'change_id', 'ordered_by', 'status', 'active_since','tenant','vpn_endpoint','remote_gateway_ip','nat_traversal','dead_pear_detection','auth_method','pre_shared_key','ike_version','accept_types','accept_peer_id','encrytion','authentication','dh_group','key_lifetime','local_id',
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
