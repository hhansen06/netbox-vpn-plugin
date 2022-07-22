from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from pkg_resources import require
from utilities.choices import ChoiceSet

from netbox.models import NetBoxModel

class VpnStatusChoices(ChoiceSet):

    STATUS_OFFLINE = 'offline'
    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_FAILED = 'failed'

    CHOICES = (
        (STATUS_OFFLINE, 'Offline', 'orange'),
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_FAILED, 'Failed', 'red'),
    )

class DeadPeerDetectionChoices(ChoiceSet):

    DISABLE = 'disable'
    ON_IDLE = 'on idle'
    ON_DEMAND = 'on demand'

    CHOICES = (
        (DISABLE, 'disable', 'red'),
        (ON_IDLE, 'on idle', 'green'),
        (ON_DEMAND, 'on demand', 'cyan'),
    )

class NatTraversalChoices(ChoiceSet):

    ENABLE = 'enable'
    DISABLE = 'disable'
    FORCED = 'forced'

    CHOICES = (
        (ENABLE, 'enable', 'red'),
        (DISABLE, 'disable', 'green'),
        (FORCED, 'forced', 'cyan'),
    )

class AuthmethodChoices(ChoiceSet):

    PSK = 'pre-shared key'
    CERT = 'certificate'

    CHOICES = (
        (PSK, 'pre-shared key', 'red'),
        (CERT, 'certificate', 'green'),
    )


class IKEVersionChoices(ChoiceSet):

    IKE_VERSION_1 = 'V1'
    IKE_VERSION_2 = 'V2' 

    CHOICES = [
        (IKE_VERSION_1, 'V1', 'red'),
        (IKE_VERSION_2, 'V2', 'green'),
    ]

class AcceptTypesChoices(ChoiceSet):
    ANY_PEER = 'any peer id'
    SPECIFIC_PEER = 'specific peer id' 

    CHOICES = [
        (ANY_PEER, 'any peer id', 'red'),
        (SPECIFIC_PEER, 'specific peer id', 'green'),
    ]

class EncryptionChoices(ChoiceSet):
    E_DES = 'DES'
    E_3DES = '3DES' 
    E_AES128 = 'AES128' 
    E_AES192 = 'AES192' 
    E_AES256 = 'AES256' 

    CHOICES = [
        (E_DES,'DES','green'),
        (E_3DES,'3DES' ,'green'),
        (E_AES128,'AES128' ,'green'),
        (E_AES192,'AES192' ,'green'),
        (E_AES256,'AES256' ,'green'),
    ]
class DhGroupChoices(ChoiceSet):
    dh_1 = "1"
    dh_2 = "2"
    dh_5 = "5"
    dh_14 = "14"
    dh_15 = "15"
    dh_16 = "16"
    dh_17 = "17"
    dh_18 = "18"
    dh_19 = "19"
    dh_20 = "20"
    dh_21 = "21"
    dh_27 = "27"
    dh_28 = "28"
    dh_29 = "29"
    dh_30 = "30"

    CHOICES = [
        (dh_1,'1','green'),
        (dh_2,'2','green'),
        (dh_5,'5','green'),
        (dh_14,'14','green'),
        (dh_15,'15','green'),
        (dh_16,'16','green'),
        (dh_17,'17','green'),
        (dh_18,'18','green'),
        (dh_19,'19','green'),
        (dh_20,'20','green'),
        (dh_21,'21','green'),
        (dh_27,'27','green'),
        (dh_28,'28','green'),
        (dh_29,'29','green'),
        (dh_30,'30','green'),
    ]

class VpnConnection(NetBoxModel):
    remote_organisation = models.CharField(
        max_length=100,
        help_text="Name of remote Organisation",
    )


    customer_contact = models.ForeignKey(
        to='tenancy.Contact',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )

    comments = models.TextField(
        blank=True,
        help_text=""
    )

    change_id = models.CharField(
        blank=True,
        max_length=100,
        null=True,
        help_text="Related change"
    )

    ordered_by = models.CharField(
        blank=True,
        max_length=100,
        null=True,
        help_text="Member who ordered the tunnel"
    )

    status = models.CharField(
        max_length=50,
        choices=VpnStatusChoices,
        default=VpnStatusChoices.STATUS_ACTIVE
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

    remote_gateway_ip = models.GenericIPAddressField(
       blank=True,
       null=True,
    )
    nat_traversal = models.CharField(
        max_length=50,
        choices=NatTraversalChoices,
        default=NatTraversalChoices.DISABLE
    )
    
    dead_pear_detection = models.CharField(
        max_length=50,
        choices=DeadPeerDetectionChoices,
        default=DeadPeerDetectionChoices.DISABLE
    )


    auth_method = models.CharField(
        max_length=50,
        choices=AuthmethodChoices,
        default=AuthmethodChoices.PSK
    )
    pre_shared_key = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    ike_version = models.CharField(
        max_length=50,
        choices=IKEVersionChoices,
        default=IKEVersionChoices.IKE_VERSION_2
    )
    accept_types = models.CharField(
        max_length=50,
        choices=AcceptTypesChoices,
        default=AcceptTypesChoices.ANY_PEER
    )
    accept_peer_id = models.CharField(
        max_length=100,
        help_text="If Accept types = specific peer ID, define remote peer Id here",
        blank=True,
        null=True,
    )


    encrytion = models.CharField(
        max_length=50,
        choices=EncryptionChoices,
        default=EncryptionChoices.E_AES256
    )
    authentication = models.CharField(
        max_length=50,
        choices=EncryptionChoices,
        default=EncryptionChoices.E_AES256
    )
    dh_group = models.CharField(
        max_length=50,
        choices=DhGroupChoices,
        blank=True,
        null=True,
    )
    key_lifetime = models.CharField(
        max_length=100,
        help_text="in Seconds",
        default= "3600"
    )
    local_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('remote_organisation',)

    def __str__(self):
        return self.remote_organisation

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpn_plugin:connection', args=[self.pk])


class VpnConnectionPhase2(NetBoxModel):
    vpn_connection = models.ForeignKey(
        to=VpnConnection,
        on_delete=models.CASCADE,
        related_name='phase2'
    )
    name = models.CharField(
        max_length=50
    )
    local_address = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
    )
    remote_address = models.CharField(
       max_length=50,
       blank=False,
       null=False,
    )
    encrytion = models.CharField(
        max_length=50,
        choices=EncryptionChoices,
        default=EncryptionChoices.E_AES256
    )
    authentication = models.CharField(
        max_length=50,
        choices=EncryptionChoices,
        default=EncryptionChoices.E_AES256
    )
    dh_group = models.CharField(
        max_length=50,
        choices=DhGroupChoices,
        blank=True,
        null=True,
    )    
    key_lifetime = models.CharField(
        max_length=100,
        help_text="in Seconds",
        default= "3600"
    )
    
    class Meta:
        ordering = ('vpn_connection', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_vpn_plugin:phase2', args=[self.pk])