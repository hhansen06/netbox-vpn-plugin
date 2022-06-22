from django.db.models import Count
from netbox.views import generic

from . import  forms, models, tables

class VpnConnectionView(generic.ObjectView):
    queryset = models.VpnConnection.objects.all()

class VpnConnectionListView(generic.ObjectListView):
    queryset = models.VpnConnection.objects.all()
    table = tables.VpnConnectionListTable


class VpnConnectionEditView(generic.ObjectEditView):
    queryset = models.VpnConnection.objects.all()
    form = forms.VpnConnectionForm


class VpnConnectionDeleteView(generic.ObjectDeleteView):
    queryset = models.VpnConnection.objects.all()
