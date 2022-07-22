from netbox.api.viewsets import NetBoxModelViewSet

from .. import  models
from .serializers import VpnConnectionPhase2Serializer, VpnConnectionSerializer


class VpnConnectionViewSet(NetBoxModelViewSet):
    queryset = models.VpnConnection.objects.prefetch_related('tags').annotate(
    )
    serializer_class = VpnConnectionSerializer

class VpnConnectionPhase2ViewSet(NetBoxModelViewSet):
    queryset = models.VpnConnectionPhase2.objects.prefetch_related('tags').annotate(
    )
    serializer_class = VpnConnectionPhase2Serializer