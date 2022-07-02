from extras.plugins import PluginConfig

class NetBoxVpnConfig(PluginConfig):
    name = 'netbox_vpn_plugin'
    verbose_name = 'VPN'
    author = "Henrik Hansen"
    author_email = "henrik.hansen@cgi.com"
    description = 'Manage VPN Configurations for Tenants'
    version = '0.8'
    base_url = 'vpn'
    
config = NetBoxVpnConfig
