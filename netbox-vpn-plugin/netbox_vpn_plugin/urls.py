
from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # Connections
    path('connection/', views.VpnConnectionListView.as_view(), name='vpnconnection_list'),
    path('connection/add/', views.VpnConnectionEditView.as_view(), name='connection_add'),
    path('connection/<int:pk>/', views.VpnConnectionView.as_view(), name='connection'),
    path('connection/<int:pk>/edit/', views.VpnConnectionEditView.as_view(), name='vpnconnection_edit'),
    path('connection/<int:pk>/delete/', views.VpnConnectionDeleteView.as_view(), name='vpnconnection_delete'),
    path('connection/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vpnconnection_changelog', kwargs={
        'model': models.VpnConnection
    }),

    #phase 2
    path('phase2/', views.VpnConnectionPhase2ListView.as_view(), name='vpnconnectionphase2_list'),
    path('phase2/add/', views.VpnConnectionPhase2EditView.as_view(), name='vpnconnectionphase2_add'),
    path('phase2/<int:pk>/', views.VpnConnectionPhase2View.as_view(), name='phase2'),
    path('phase2/<int:pk>/edit/', views.VpnConnectionPhase2EditView.as_view(), name='vpnconnectionphase2_edit'),
    path('phase2/<int:pk>/delete/', views.VpnConnectionPhase2DeleteView.as_view(), name='vpnconnectionphase2_delete'),
    path('phase2/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vpnconnectionphase2_changelog', kwargs={
        'model': models.VpnConnectionPhase2
    }),
)