
from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('vpn-lists/', views.VpnView.as_view(), name='vpn_list'),
    path('vpn-lists/add/', views.VpnEditView.as_view(), name='vpnlist_add'),
    path('vpn-lists/<int:pk>/', views.VpnListView.as_view(), name='vpndetails'),
    path('vpn-lists/<int:pk>/edit/', views.VpnEditView.as_view(), name='vpnlist_edit'),
    path('vpn-lists/<int:pk>/delete/', views.VpnDeleteView.as_view(), name='vpnlist_delete'),
    path('vpn-lists/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vpnlist_changelog', kwargs={
        'model': models.Vpn
    }),
)