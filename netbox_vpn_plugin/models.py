from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel

class VpnConnection(NetBoxModel):
    gegenstelle = models.CharField(
        max_length=100
    )
    comments = models.TextField(
        blank=True
    )

    ordered_by = models.TextField(
        blank=True,
        null=True
    )

    active_since = models.DateField(
        blank=True,
        null=True
    )

    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='+',
        blank=False,
        null=False
    )

    vpn_endpoint = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='+',
        blank=False,
        null=True
    )

    remote_ip = models.GenericIPAddressField(
       blank=True, null=True
    )

    customer_contact = models.ForeignKey(
        to='tenancy.Contact',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )
    
    class Meta:
        ordering = ('gegenstelle',)

    def __str__(self):
        return self.gegenstelle

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpn_plugin:connection', args=[self.pk])