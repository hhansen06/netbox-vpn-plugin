from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


connectionlist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_vpn_plugin:connection_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
menu_items = (
    PluginMenuItem(
        link='plugins:netbox_vpn_plugin:vpnconnection_list',
        link_text='VPN Connections',
        buttons=connectionlist_buttons
        
    ),
)