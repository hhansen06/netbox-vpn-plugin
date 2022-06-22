from django.db.models import Count
from netbox.views import generic

from . import  forms, models, tables

class VpnView(generic.ObjectView):
    queryset = models.Vpn.objects.all()

class VpnListView(generic.ObjectListView):
    table = tables.VpnListTable


class VpnEditView(generic.ObjectEditView):
    queryset = models.Vpn.objects.all()
    form = forms.VpnForm


class VpnDeleteView(generic.ObjectDeleteView):
    queryset = models.Vpn.objects.all()
