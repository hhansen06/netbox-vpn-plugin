
from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('connection/', views.VpnConnectionListView.as_view(), name='vpnconnection_list'),
    path('connection/add/', views.VpnConnectionEditView.as_view(), name='connection_add'),
    path('connection/<int:pk>/', views.VpnConnectionView.as_view(), name='connection'),
    path('connection/<int:pk>/edit/', views.VpnConnectionEditView.as_view(), name='vpnconnection_edit'),
    path('connection/<int:pk>/delete/', views.VpnConnectionDeleteView.as_view(), name='vpnconnection_delete'),
    path('connection/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vpnconnection_changelog', kwargs={
        'model': models.VpnConnection
    }),
)