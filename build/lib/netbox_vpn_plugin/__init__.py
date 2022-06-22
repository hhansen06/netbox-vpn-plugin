from extras.plugins import PluginConfig

class NetBoxVpnConfig(PluginConfig):
    name = 'netbox_vpn_plugin'
    verbose_name = ' NetBox VPN Plugin'
    author = "Henrik Hansen"
    author_email = "henrik.hansen@cgi.com"
    description = 'Manage VPN Configurations for Tenants'
    version = '0.3'
    base_url = 'vpn'
    
config = NetBoxVpnConfig
