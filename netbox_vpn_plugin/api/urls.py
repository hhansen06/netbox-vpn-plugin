from netbox.api.routers import NetBoxRouter
from . import views


app_name = 'netbox_vpn_plugin'

router = NetBoxRouter()
router.register('connections', views.VpnConnectionViewSet)

urlpatterns = router.urls