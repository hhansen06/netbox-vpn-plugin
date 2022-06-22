from netbox.api.viewsets import NetBoxModelViewSet

from .. import  models
from .serializers import VpnConnectionSerializer


class VpnConnectionViewSet(NetBoxModelViewSet):
    queryset = models.VpnConnection.objects.prefetch_related('tags').annotate(
    )
    serializer_class = VpnConnectionSerializer