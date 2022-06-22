## netbox-vpn-plugin

Manage Vpn Connections for Tenants in Netbox.


Adding Test Data:
NBSHELL:

device = Device.objects.get(pk=1)
tenant = Tenant.objects.get(pk=1)
from netbox_vpn_plugin.models import *
vpn = VpnList(gegenstelle="abc",orginator=device,tenant=tenant)
vpn.save()