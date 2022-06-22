from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

class Vpn(NetBoxModel):
    gegenstelle = models.CharField(
        max_length=100
    )
    comments = models.TextField(
        blank=True
    )
    
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='+',
        blank=False,
        null=False
    )

    orginator = models.ForeignKey(
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
        return reverse('plugins:netbox_vpn_plugin:vpn_list', args=[self.pk])

    def get_default_action_color(self):
        return ActionChoices.colors.get(self.default_action)