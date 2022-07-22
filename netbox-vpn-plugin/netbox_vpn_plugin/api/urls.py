from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_vpn_plugin'

router = NetBoxRouter()
router.register('connection', views.VpnConnectionViewSet)
router.register('phase2', views.VpnConnectionPhase2ViewSet)

urlpatterns = router.urls