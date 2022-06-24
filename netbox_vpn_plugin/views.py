from django.db.models import Count
from extras.plugins import PluginTemplateExtension
from netbox.views import generic
from netbox_vpn_plugin.filtersets import VpnConnectionFilterSet
from . import  forms, models, tables

class VpnConnectionView(generic.ObjectView):
    queryset = models.VpnConnection.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.VpnConnectionPhase2Table (instance.phase2.all())
        table.configure(request)

        return {
            'phase2_table': table,
        }

class VpnConnectionListView(generic.ObjectListView):
    queryset = models.VpnConnection.objects.all()
    filterset = VpnConnectionFilterSet
    filterset_form = forms.VpnConnectionFilterForm

    action_buttons = ('add',)  
    table = tables.VpnConnectionListTable

class VpnConnectionEditView(generic.ObjectEditView):
    queryset = models.VpnConnection.objects.all()
    form = forms.VpnConnectionForm


class VpnConnectionDeleteView(generic.ObjectDeleteView):
    queryset = models.VpnConnection.objects.all()


# PHase 2

class VpnConnectionPhase2View(generic.ObjectView):
     
    queryset = models.VpnConnectionPhase2.objects.all()
    table = tables.VpnConnectionPhase2Table

class VpnConnectionPhase2ListView(generic.ObjectListView):
    action_buttons = ('add',)  
    queryset = models.VpnConnectionPhase2.objects.all()
    table = tables.VpnConnectionListTable


class VpnConnectionPhase2EditView(generic.ObjectEditView):
    queryset = models.VpnConnectionPhase2.objects.all()
    form = forms.VpnConnectionPhase2Form


class VpnConnectionPhase2DeleteView(generic.ObjectDeleteView):
    queryset = models.VpnConnectionPhase2.objects.all()